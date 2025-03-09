from langchain_community.document_loaders import WebBaseLoader

def scrape_web(url):
    loader = WebBaseLoader(url)
    documents = loader.load()
    return documents