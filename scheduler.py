from apscheduler.schedulers.background import BackgroundScheduler
from x_service import TwitterService
import time

twitter = TwitterService()
scheduler = BackgroundScheduler()

def auto_tweet():
    twitter.post_tweet("This is an automated tweet!")

scheduler.add_job(auto_tweet, "cron", hour=9, minute=0)  # Every day 9 AM
scheduler.start()

print("🕒 Scheduler running... Press Ctrl+C to stop.")
try:
    while True:
        time.sleep(60)
except KeyboardInterrupt:
    scheduler.shutdown()
    print("Scheduler stopped.")
