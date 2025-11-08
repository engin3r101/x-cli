import tweepy
import os
from dotenv import load_dotenv
import csv
from datetime import datetime

load_dotenv()

client = tweepy.Client(bearer_token=os.getenv("BEARER_TOKEN"))

user = client.get_user(username=os.getenv("X_USERNAME"))
tweets = client.get_users_tweets(
    id=user.data.id, 
    max_results=50,
    tweet_fields=['created_at', 'public_metrics']  # Get additional tweet metadata
)

csv_filename = "tweets.csv"

# Write tweets to CSV
with open(csv_filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(['Tweet ID', 'Created At', 'Text', 'Likes', 'Retweets', 'Replies'])
    
    # Write tweet data
    for tweet in tweets.data:
        writer.writerow([
            tweet.id,
            tweet.created_at,
            tweet.text,
            tweet.public_metrics['like_count'],
            tweet.public_metrics['retweet_count'],
            tweet.public_metrics['reply_count']
        ])

print(f"Tweets have been saved to {csv_filename}")