import credentials
import tweepy

API_KEY = credentials.TWITTER_API_KEY
API_SECRET = credentials.TWITTER_API_SECRET_KEY
ACCESS_TOKEN = credentials.TWITTER_ACCESS_TOKEN
ACCESS_TOKEN_SECRET = credentials.TWITTER_ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

def get_cramer_tweets():
    # Authenticate to Twitter API
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # Create Tweepy API object
    api = tweepy.API(auth)

    # Fetch Cramer's tweets
    tweets = api.user_timeline(screen_name='jimcramer', count=10)

    # Return list of tweet objects
    return tweets
