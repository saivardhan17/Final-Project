def load_faq_content(url):
    import requests
    from bs4 import BeautifulSoup
    from langchain_core.documents import Document

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = [p.get_text() for p in soup.find_all("p")]
    full_text = " ".join(paragraphs)
    return [Document(page_content=full_text)]