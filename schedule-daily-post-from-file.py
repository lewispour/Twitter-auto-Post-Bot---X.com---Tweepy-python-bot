import tweepy
import datetime
import random
import keys
import schedule
import time

# Initialize Tweepy
client = tweepy.Client(keys.bearer_token, keys.api_key, keys.api_secret, keys.access_token, keys.access_token_secret)
auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret, keys.access_token, keys.access_token_secret)
api = tweepy.API(auth)

def sendPost():
    # Get the current date and time
    current_date = datetime.date.today()

    # Format the date as a string
    formatted_date = current_date.strftime("%B %d, %Y")

    # Read lines from the file
    with open('tweets.txt', 'r') as file:
        lines = file.readlines()

    # Choose a random line and remove any leading/trailing whitespace
    tweet_text = random.choice(lines).strip()

    # Send the tweet
    client.create_tweet(text=f"{tweet_text}")

    # Print a message to indicate that the request was successful
    print("Tweet posted successfully")

# Schedule the job every day at 9 AM
schedule.every().day.at("09:00").do(sendPost)

# Loop to keep the script running
while True:
    schedule.run_pending()
    time.sleep(60)  # Wait for one minute before checking again
