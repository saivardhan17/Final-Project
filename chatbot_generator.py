def chatbot_workflow():
    import streamlit as st
    from parsing_utils import load_faq_content
    from embedding_utils import embed_and_store
    from langchain.llms import OpenAI
    from langchain.chains import RetrievalQA

    st.header("Chatbot Generator from FAQ")
    url = st.text_input("Enter FAQ URL")
    if url:
        faq_content = load_faq_content(url)
        vectorstore = embed_and_store(faq_content)
        retriever = vectorstore.as_retriever()
        llm = OpenAI(temperature=0.3)
        qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

        user_query = st.text_input("Ask your support question:")
        if user_query:
            response = qa_chain.run(user_query)
            st.write(response)
