import sys
from x_service import TwitterService

if len(sys.argv) < 2:
    print("Usage: python cli.py 'Your tweet message'")
    sys.exit(1)

message = sys.argv[1]
twitter = TwitterService()
twitter.post_tweet(message)
