import sys
import os
import random
import schedule
import time

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'config'))
import keys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from functions import initialize_tweepy, get_formatted_date

def send_post():
    client, _ = initialize_tweepy()
    
    with open(os.path.join(os.path.dirname(__file__), '..', 'data', 'tweets.txt'), 'r') as file:
        lines = file.readlines()
    tweet_text = random.choice(lines).strip()
    client.create_tweet(text=f"{tweet_text}")

    print("Tweet posted successfully")

schedule.every().day.at("09:00").do(send_post)

while True:
    schedule.run_pending()
    time.sleep(60)
