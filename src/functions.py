import tweepy
import datetime
import sys
from openai import OpenAI
sys.path.append('../config')
import keys  


def initialize_tweepy():
    client = tweepy.Client(keys.bearer_token, keys.api_key, keys.api_secret, keys.access_token, keys.access_token_secret)
    auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret, keys.access_token, keys.access_token_secret)
    api = tweepy.API(auth)
    return client, api

def get_formatted_date():
    current_date = datetime.date.today()
    return current_date.strftime("%B %d, %Y")

def generate_response(prompt):
    client = OpenAI(api_key=keys.openai_key)
    model = "gpt-4-1106-preview"
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )

    response_message = response.choices[0].message.content
    return response_message.strip()