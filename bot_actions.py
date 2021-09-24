import tweepy
from credentials import *

# setting the api key and secret of the app
auth = tweepy.OAuthHandler(consumer_api_key, consumer_api_key_secret)

# setting the access token and secret of the concerned account
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def test_api():
    print("GDSC twitter bot")
    user = api.me()
    print(user.name)


def reply_tweet(search, num_of_tweets, response):
    for tweet in tweepy.Cursor(api.search, search).items(num_of_tweets):
        try:
            tweet_id = tweet.user.id
            username = tweet.user.screen_name
            '''reply to the tweet'''
            print("\nTweet by: @{}".format(username))
            print("ID: @{}".format(str(tweet_id)))

            api.update_status("@{} {}".format(username, response), in_reply_to_status_id=tweet_id)
            print("Replied with: {}".format(response))

        except tweepy.TweepError as te:
            print(te.reason)
        except StopIteration:
            break


def retweet_tweet(search, num_of_tweets):
    for tweet in tweepy.Cursor(api.search, search).items(num_of_tweets):
        try:
            '''retweet the tweet'''
            tweet.retweet()
            print("Retweeted the tweet")

        except tweepy.TweepError as te:
            print(te.reason)
        except StopIteration:
            break


def fav_tweet(search, num_of_tweets):
    for tweet in tweepy.Cursor(api.search, search).items(num_of_tweets):
        try:
            '''fav the tweet'''
            tweet.favorite()
            print("Favorite the tweet")

        except tweepy.TweepError as te:
            print(te.reason)
        except StopIteration:
            break


def follow_user(search, num_of_tweets):
    for tweet in tweepy.Cursor(api.search, search).items(num_of_tweets):
        try:
            '''follow the tweet'''
            tweet.user.follow()
            print("Followed the user")

        except tweepy.TweepError as te:
            print(te.reason)
        except StopIteration:
            break
