import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob


class TwitterClient(object):
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.auth = OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth)

    def clean_tweet(self, tweet):
        # Your clean_tweet method remains the same
        pass

    def get_tweet_sentiment(self, tweet):
        # Your get_tweet_sentiment method remains the same
        pass

    def get_tweets(self, query, count=10):
        tweets = []
        try:
            for tweet in tweepy.Cursor(self.api.search, q=query, tweet_mode="extended").items(count):
                parsed_tweet = {
                    'text': self.clean_tweet(tweet.full_text),
                    'sentiment': self.get_tweet_sentiment(tweet.full_text)
                }
                tweets.append(parsed_tweet)
            return tweets
        except tweepy.TweepError as e:
            print("Error: " + str(e))


def main():
    consumer_key = 'tZavWVFQOTZf63DZ0dL45Aj2Z'
    consumer_secret = 'V5Un8Ku8iEEGJ76bYN4UHYsSowFuzf3lSxnCwPqLgx1SDfU2oU'
    access_token = '1704163527769116672-CNrFtvATMJjCab3ffDNIxlt8Bg3nNz'
    access_token_secret = 'TIZGg91vNuJXeUtAl5JRLufNKU5oGO4AwsrcFXaq9piax'

    query = input("Enter a keyword for sentiment analysis: ")
    count = int(input("Enter the number of tweets to analyze: "))

    analyzer = TwitterClient(
        consumer_key, consumer_secret, access_token, access_token_secret)
    tweets = analyzer.get_tweets(query=query, count=count)

    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']

    print("Positive tweets percentage: {:.2f}%".format(
        100 * len(ptweets) / len(tweets)))
    print("Negative tweets percentage: {:.2f}%".format(
        100 * len(ntweets) / len(tweets)))
    print("Neutral tweets percentage: {:.2f}%".format(
        100 * (len(tweets) - (len(ntweets) + len(ptweets))) / len(tweets)))

    print("\nPositive tweets:")
    for tweet in ptweets[:10]:
        print(tweet['text'])

    print("\nNegative tweets:")
    for tweet in ntweets[:10]:
        print(tweet['text'])


if __name__ == "__main__":
    main()
