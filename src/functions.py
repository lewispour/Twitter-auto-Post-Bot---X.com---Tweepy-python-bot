import tweepy
import datetime
import sys
sys.path.append('../config')  # Adds the config directory to the path
import keys  # Now we can import keys

def initialize_tweepy():
    client = tweepy.Client(keys.bearer_token, keys.api_key, keys.api_secret, keys.access_token, keys.access_token_secret)
    auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret, keys.access_token, keys.access_token_secret)
    api = tweepy.API(auth)
    return client, api

def get_formatted_date():
    current_date = datetime.date.today()
    return current_date.strftime("%B %d, %Y")
