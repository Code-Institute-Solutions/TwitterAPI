import json
import tweepy
from tweepy import OAuthHandler


CONSUMER_KEY = 'your_consumer_key'
CONSUMER_SECRET = 'your_consumer_secret_key'
OAUTH_TOKEN = 'your-oauth-token'
OAUTH_TOKEN_SECRET = 'your-oauth-token-secret'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

count = 10
query = 'Dublin'

# Get all status
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

for result in results:
    print(json.dumps(result._json, indent=4))

for status in results:
    print(status.text.encode('utf-8'))
    print(status.user.id)
    print(status.user.screen_name)
    print(status.user.followers_count)
    print(status.place)

