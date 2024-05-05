import json
import openai
from dotenv import load_dotenv
load_dotenv()
import os 

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
openai.api_key = os.getenv("OPENAI_API_KEY")


def analyze_sentiment(review, system_prompt):

    response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": review},
    ])

    sentiment = response['choices'][0]['message']['content']
    json_sentiment = json.loads(sentiment)

    return json_sentiment.get("response")