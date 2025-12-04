#!/usr/bin/env python3
"""
Twitter Auto-Post Bot Web Interface
A browser-based interface for managing automated Twitter posts.
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
import sys
import os
import random
import json
import threading
import schedule
import time
from datetime import datetime

sys.path.append(os.path.join(os.path.dirname(__file__), 'config'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

import keys
from src.functions import generate_response, initialize_tweepy, get_formatted_date

app = Flask(__name__)
app.secret_key = 'twitter-bot-secret-key-change-in-production'

# Global variable to track scheduler
scheduler_running = False
scheduler_thread = None
scheduled_jobs = []


def get_tweets_from_file():
    """Read all tweets from the tweets.txt file."""
    tweets_file = os.path.join(os.path.dirname(__file__), 'data', 'tweets.txt')
    if not os.path.exists(tweets_file):
        return []

    with open(tweets_file, 'r') as file:
        return [line.strip() for line in file.readlines() if line.strip()]


def save_tweets_to_file(tweets):
    """Save tweets to the tweets.txt file."""
    tweets_file = os.path.join(os.path.dirname(__file__), 'data', 'tweets.txt')
    os.makedirs(os.path.dirname(tweets_file), exist_ok=True)

    with open(tweets_file, 'w') as file:
        for tweet in tweets:
            file.write(tweet + '\n')


@app.route('/')
def index():
    """Dashboard page."""
    return render_template('index.html', scheduler_running=scheduler_running, scheduled_jobs=scheduled_jobs)


@app.route('/test-credentials', methods=['POST'])
def test_credentials():
    """Test Twitter API credentials."""
    try:
        client, api = initialize_tweepy()
        user = api.verify_credentials()

        return jsonify({
            'success': True,
            'data': {
                'username': user.screen_name,
                'name': user.name,
                'followers': user.followers_count,
                'following': user.friends_count
            }
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400


@app.route('/post')
def post_page():
    """Post tweet page."""
    return render_template('post.html')


@app.route('/post-tweet', methods=['POST'])
def post_tweet():
    """Post a tweet instantly."""
    try:
        data = request.get_json()
        tweet_type = data.get('type')

        client, _ = initialize_tweepy()

        if tweet_type == 'ai':
            prompt = data.get('prompt', 'Create a short tweet about Motorbikes.')
            tweet_text = generate_response(prompt)
        elif tweet_type == 'file':
            tweets = get_tweets_from_file()
            if not tweets:
                return jsonify({'success': False, 'error': 'No tweets found in file'}), 400
            tweet_text = random.choice(tweets)
        elif tweet_type == 'text':
            tweet_text = data.get('text')
            if not tweet_text:
                return jsonify({'success': False, 'error': 'No text provided'}), 400
        else:
            return jsonify({'success': False, 'error': 'Invalid tweet type'}), 400

        client.create_tweet(text=tweet_text)

        return jsonify({
            'success': True,
            'tweet': tweet_text
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400


@app.route('/manage-tweets')
def manage_tweets():
    """Manage tweets page."""
    tweets = get_tweets_from_file()
    return render_template('manage_tweets.html', tweets=tweets)


@app.route('/add-tweet', methods=['POST'])
def add_tweet():
    """Add a new tweet to the file."""
    try:
        data = request.get_json()
        tweet = data.get('tweet', '').strip()

        if not tweet:
            return jsonify({'success': False, 'error': 'Tweet cannot be empty'}), 400

        tweets = get_tweets_from_file()
        tweets.append(tweet)
        save_tweets_to_file(tweets)

        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400


@app.route('/delete-tweet', methods=['POST'])
def delete_tweet():
    """Delete a tweet from the file."""
    try:
        data = request.get_json()
        index = data.get('index')

        tweets = get_tweets_from_file()
        if 0 <= index < len(tweets):
            tweets.pop(index)
            save_tweets_to_file(tweets)
            return jsonify({'success': True})
        else:
            return jsonify({'success': False, 'error': 'Invalid index'}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400


@app.route('/update-tweet', methods=['POST'])
def update_tweet():
    """Update a tweet in the file."""
    try:
        data = request.get_json()
        index = data.get('index')
        new_text = data.get('text', '').strip()

        if not new_text:
            return jsonify({'success': False, 'error': 'Tweet cannot be empty'}), 400

        tweets = get_tweets_from_file()
        if 0 <= index < len(tweets):
            tweets[index] = new_text
            save_tweets_to_file(tweets)
            return jsonify({'success': True})
        else:
            return jsonify({'success': False, 'error': 'Invalid index'}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400


@app.route('/schedule')
def schedule_page():
    """Schedule tweets page."""
    return render_template('schedule.html', scheduled_jobs=scheduled_jobs, scheduler_running=scheduler_running)


def run_scheduler():
    """Run the scheduler in a separate thread."""
    global scheduler_running
    while scheduler_running:
        schedule.run_pending()
        time.sleep(60)


@app.route('/start-schedule', methods=['POST'])
def start_schedule():
    """Start scheduled tweets."""
    global scheduler_running, scheduler_thread, scheduled_jobs

    try:
        data = request.get_json()
        schedule_type = data.get('type')
        schedule_time = data.get('time', '09:00')
        prompt = data.get('prompt', 'Create a short tweet about Motorbikes.')

        if scheduler_running:
            return jsonify({'success': False, 'error': 'Scheduler is already running'}), 400

        # Clear existing jobs
        schedule.clear()
        scheduled_jobs = []

        client, _ = initialize_tweepy()

        if schedule_type == 'ai':
            def send_ai_post():
                try:
                    response = generate_response(prompt)
                    client.create_tweet(text=response)
                    print(f'Posted tweet: {response}')
                except Exception as e:
                    print(f'Error posting tweet: {str(e)}')

            schedule.every().day.at(schedule_time).do(send_ai_post)
            scheduled_jobs.append({
                'type': 'AI Generated',
                'time': schedule_time,
                'prompt': prompt
            })

        elif schedule_type == 'file':
            def send_file_post():
                try:
                    tweets = get_tweets_from_file()
                    if tweets:
                        tweet_text = random.choice(tweets)
                        client.create_tweet(text=tweet_text)
                        print(f'Posted tweet: {tweet_text}')
                except Exception as e:
                    print(f'Error posting tweet: {str(e)}')

            schedule.every().day.at(schedule_time).do(send_file_post)
            scheduled_jobs.append({
                'type': 'Random from File',
                'time': schedule_time,
                'prompt': 'N/A'
            })

        scheduler_running = True
        scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
        scheduler_thread.start()

        return jsonify({'success': True, 'message': f'Scheduler started for {schedule_time}'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400


@app.route('/stop-schedule', methods=['POST'])
def stop_schedule():
    """Stop scheduled tweets."""
    global scheduler_running, scheduled_jobs

    scheduler_running = False
    schedule.clear()
    scheduled_jobs = []

    return jsonify({'success': True, 'message': 'Scheduler stopped'})


@app.route('/scheduler-status')
def scheduler_status():
    """Get scheduler status."""
    return jsonify({
        'running': scheduler_running,
        'jobs': scheduled_jobs
    })


if __name__ == '__main__':
    print("Starting Twitter Bot Web Interface...")
    print("Open your browser and navigate to: http://localhost:8080")
    app.run(debug=True, host='0.0.0.0', port=8080)
