import tweepy
from tweepy import OAuthHandler


CONSUMER_KEY = 'your_consumer_key'
CONSUMER_SECRET = 'your_consumer_secret_key'
OAUTH_TOKEN = 'your-oauth-token'
OAUTH_TOKEN_SECRET = 'your-oauth-token-secret'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a tweet
    print(status.text)
