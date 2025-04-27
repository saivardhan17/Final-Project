try:
    def embed_and_store(documents):
        from langchain_openai import OpenAIEmbeddings
        from langchain.vectorstores import FAISS
        import openai


        embeddings = OpenAIEmbeddings(openai_api_key="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")
        vectorstore = FAISS.from_documents(documents, embeddings)
        return vectorstore
except openai.RateLimitError as e:
    print("Rate limit exceeded. Please check your OpenAI account quota.")


