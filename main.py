import tweepy
import requests
import json
import time

# Define Twitter API keys and access tokens
consumer_key = "YOUR_CONSUMER_KEY_HERE"
consumer_secret = "YOUR_CONSUMER_SECRET_HERE"
access_token = "YOUR_ACCESS_TOKEN_HERE"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET_HERE"

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Define the hashtag to search for and the official Pixels Twitter account
search_query = "#wenpixel OR to:official_pixels"

# Define the URL of the mock API to send data to
mock_api_url = "https://your-mock-api-url.com/wen"

# Define a function to process tweets and send data to the API
def process_tweet(tweet):
    # Extract the user ID and tweet ID
    user_id = tweet.user.id_str
    tweet_id = tweet.id_str

    # Send a POST request to the mock API with the user ID and tweet ID
    headers = {"Content-Type": "application/json"}
    data = {"user_id": user_id, "tweet_id": tweet_id}
    response = requests.post(mock_api_url, data=json.dumps(data), headers=headers)

    # Print the response from the API
    print(response.json())

# Define a function to run the scraper
def run_scraper():
    # Search for tweets that match the search query
    tweets = tweepy.Cursor(api.search_tweets, q=search_query).items()

    # Loop through the tweets and process them
    for tweet in tweets:
        process_tweet(tweet)

        # Wait for 5 seconds to avoid hitting Twitter API rate limit
        time.sleep(5)

# Run the scraper
run_scraper()
