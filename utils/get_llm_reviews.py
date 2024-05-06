import json
import openai
import streamlit as st
import os 

openai.api_key = st.secrets["OPENAI_API_KEY"]
print(openai.api_key)


def analyze_sentiment(review, system_prompt):
    """
    Analyzes the sentiment of a given review using the OpenAI GPT-4 API.

    This function sends a review and a system prompt to the OpenAI GPT-4 model
    and receives a sentiment analysis response. The response is then parsed
    from JSON format to extract the sentiment result.

    Args:
        review (str): The text of the review to analyze.
        system_prompt (str): The system prompt that provides context to the model.

    Returns:
        str: The sentiment response extracted from the model's output, or None
             if the response could not be extracted.
    """

    response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": review},
    ])

    sentiment = response['choices'][0]['message']['content']
    json_sentiment = json.loads(sentiment)

    return json_sentiment.get("response")