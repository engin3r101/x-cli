# import pandas as pd
# import numpy as np
# import re
# df = pd.read_csv('tweets_20251108_114649.csv')
# # print(df.head())
# # print(df.info())
# texts = df['Text'].tolist()
# print(texts)

import pandas as pd
from groq import Groq
import os

from dotenv import load_dotenv

load_dotenv()

# Read the CSV file
df = pd.read_csv('tweets.csv')

# Filter tweets containing #LearnInPublic or learning-related content
learning_tweets = df[df['Text'].str.contains('Learnt|#LearnInPublic', case=False, na=False)]
learning_texts = learning_tweets['Text'].tolist()

# Combine all learning tweets into one string
combined_tweets = "\n".join(learning_texts)

# Initialize Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Create the prompt for summarization
prompt = f"""You are an expert at summarizing learning content from tweets.
Given the following tweets where the user shares what they have learned, extract and summarize the key learnings. 
Here are the tweets:
{combined_tweets}
Provide a concise summary of the main learnings in bullet points.
An example output format:
- Learning Point 1 : The user has learnt about LLMs.
- Learning Point 2 : The user has learnt to interact with X apis by building a project that hits the get_tweets and create_tweet apis via Tweepy.
"""

# Make the API call
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    model="openai/gpt-oss-120b",  # Using Mixtral model via Groq
    temperature=0.3
)

# Print the summarized response
print("\nSummary of Learnings:")
print(chat_completion.choices[0].message.content)
