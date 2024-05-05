import pandas as pd
from utils.get_llm_reviews import analyze_sentiment

from prompts.Sentiment_Analysis import system_prompt

df_reviews = pd.read_csv("./data/item_reviews.csv")

results = {}
for i, row in enumerate(df_reviews):
    review = df_reviews.loc[i,"content"]
    sentiment = df_reviews.loc[i,"sentiment"]
    predicted_sentiment = analyze_sentiment(review, system_prompt)

    results[i] = {
        "review": review,
        "actual_sentiment": sentiment,
        "predicted_sentiment": predicted_sentiment
    }

    print(results)
    