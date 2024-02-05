import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'config'))
import keys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from functions import initialize_tweepy, get_formatted_date

def send_post():
    client, _ = initialize_tweepy()
    formatted_date = get_formatted_date()

    client.create_tweet(text=f"Hello Python 🐍. It is {formatted_date} today!🚀🚀.")
    print("Tweet posted successfully")

send_post()
