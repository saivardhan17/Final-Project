def sentiment_workflow():
    import streamlit as st
    from langchain.chat_models import ChatOpenAI

    st.header("Customer Sentiment Analyzer")
    uploaded_file = st.file_uploader("Upload review file (txt)")
    if uploaded_file:
        reviews = uploaded_file.read().decode("utf-8").split("\n")
        llm = ChatOpenAI(temperature=0, openai_api_key="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")
        sentiments = []
        for review in reviews:
            prompt = f"Classify this review as Positive, Neutral, or Negative and explain why:\n{review}"
            sentiment = llm.predict(prompt)
            sentiments.append((review, sentiment))

        for r, s in sentiments:
            st.write(f"**Review:** {r}")
            st.write(f"**Sentiment:** {s}")