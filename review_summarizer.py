def summarizer_workflow():
    import streamlit as st
    from langchain.chat_models import ChatOpenAI

    st.header("Product Review Summarizer")
    uploaded_file = st.file_uploader("Upload review file (txt)")
    if uploaded_file:
        reviews = uploaded_file.read().decode("utf-8")
        llm = ChatOpenAI(temperature=0.2, openai_api_key="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")
        prompt = f"Summarize the following customer reviews into key points with pros and cons:\n{reviews}"
        summary = llm.predict(prompt)
        st.write(summary)