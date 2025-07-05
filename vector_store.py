from langchain_community.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader
import os

def get_vectorstore():
    loader = TextLoader("data/memory.txt")
    docs = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(docs)
    embeddings = OpenAIEmbeddings()
    return FAISS.from_documents(docs, embeddings)