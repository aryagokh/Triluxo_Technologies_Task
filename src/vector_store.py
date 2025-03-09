from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter

embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

def load_faiss():
    return FAISS.load_local("vector_store", embeddings, allow_dangerous_deserialization=True)

def store_embeddings(documents):

    if not documents:
        print("No data extracted.")
        return
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=25)
    split_docs = text_splitter.split_documents(documents)

    vector_db = FAISS.from_documents(split_docs, embeddings)
    vector_db.save_local("vector_store")
    print("Embeddings stored successfully.")