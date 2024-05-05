import json
import openai
import streamlit as st
from dotenv import load_dotenv
import os 


openai.api_key = st.secrets("OPENAI_API_KEY")
print(openai.api_key)


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