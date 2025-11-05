import os
import tweepy
from dotenv import load_dotenv

load_dotenv()

# For API v2, you need Bearer Token OR OAuth 1.0a credentials
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
API_KEY = os.getenv("API_KEY")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

class TwitterService:
    def __init__(self):
        try:
            # Using OAuth 1.0a for user context (required for posting)
            # API v2 Client with OAuth 1.0a authentication
            self.client = tweepy.Client(
                bearer_token=BEARER_TOKEN,
                consumer_key=API_KEY,
                consumer_secret=API_SECRET_KEY,
                access_token=ACCESS_TOKEN,
                access_token_secret=ACCESS_TOKEN_SECRET
            )
            
            # Verify credentials
            user = self.client.get_me()
            if user.data:
                print(f"✅ Twitter authentication successful as @{user.data.username}")
            else:
                print("✅ Twitter authentication successful.")
                
        except Exception as e:
            print(f"❌ Twitter authentication failed: {e}")
            raise

    def post_tweet(self, message: str):
        try:
            # Using API v2 create_tweet method
            response = self.client.create_tweet(text=message)
            
            tweet_id = response.data['id']
            print(f"🐦 Tweet posted successfully!")
            print(f"   Message: {message}")
            print(f"   Tweet ID: {tweet_id}")
            print(f"   URL: https://twitter.com/user/status/{tweet_id}")
            
            return {
                "status": "success", 
                "message": message, 
                "tweet_id": tweet_id
            }
            
        except tweepy.TweepyException as e:
            print(f"⚠️ Tweet failed: {e}")
            
            # Specific error handling
            if "403" in str(e):
                print("\n💡 Troubleshooting:")
                print("   1. Verify you have 'Read and Write' permissions")
                print("   2. Make sure you regenerated tokens after permission change")
                print("   3. Check you haven't exceeded 500 posts/month limit")
                print("   4. Visit: https://developer.x.com/en/portal/dashboard")
            
            return {"status": "error", "error": str(e)}