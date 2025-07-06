
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

def get_vectorstore():
    return FAISS.load_local("vector_index", OpenAIEmbeddings())
