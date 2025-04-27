def marketing_workflow():
    import streamlit as st
    from langchain.chat_models import ChatOpenAI

    st.header("Marketing Copy Generator")
    product_description = st.text_area("Enter Product Description")
    tone = st.selectbox("Select Tone", ("Fun", "Professional", "Luxury"))
    if st.button("Generate Marketing Copy"):
        llm = ChatOpenAI(temperature=0.5, openai_api_key="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")
        prompt = f"Write an Instagram caption for the following product in a {tone} tone:\n{product_description}"
        marketing_copy = llm.predict(prompt)
        st.write(marketing_copy)