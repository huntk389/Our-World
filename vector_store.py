from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
import os

def get_vectorstore():
    if not os.path.exists(".vector/index"):
        from langchain.document_loaders import TextLoader
        from langchain.text_splitter import RecursiveCharacterTextSplitter
        from langchain.vectorstores.faiss import FAISS

        loader = TextLoader("docs.txt")
        documents = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        texts = text_splitter.split_documents(documents)
        embeddings = OpenAIEmbeddings()
        vectordb = FAISS.from_documents(texts, embeddings)
        vectordb.save_local(".vector")
    return FAISS.load_local(".vector", OpenAIEmbeddings())