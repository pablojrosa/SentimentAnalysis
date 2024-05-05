import streamlit as st
from utils.get_llm_reviews import analyze_sentiment
from prompts.Sentiment_Analysis import system_prompt

def main():
    st.title("Analisis de sentimientos de reviews de productos")
    st.subheader("Ingresa su review:")

    user_input = st.text_area("Review:")
    
    if st.button("Analizar"):
        result = analyze_sentiment(user_input, system_prompt)
        if result == "Positive":
            st.success("Sentimiento: Positivo 👍")
        else:
            st.error("Sentimiento: Negativo  👎")

if __name__ == "__main__":
    main()
