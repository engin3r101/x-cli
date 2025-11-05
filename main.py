from fastapi import FastAPI, Header, HTTPException
from x_service import TwitterService

app = FastAPI(title="Local Twitter Bot")

twitter = TwitterService()

# Set a local API key for security
API_AUTH_KEY = "local-secret-key"

@app.post("/tweet")
def post_tweet(message: str, x_api_key: str = Header(None)):
    if x_api_key != API_AUTH_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

    return twitter.post_tweet(message)
