
import os
from pathlib import Path
from langchain_community.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader, DirectoryLoader

VECTOR_DIR = "data/vector_index"
SOURCE_DIR = "story"

def get_vectorstore():
    if Path(VECTOR_DIR).exists():
        return FAISS.load_local(VECTOR_DIR, OpenAIEmbeddings(), allow_dangerous_deserialization=True)

    if not Path(SOURCE_DIR).exists():
        raise FileNotFoundError("No memory source directory found for RAG.")

    loader = DirectoryLoader(SOURCE_DIR, glob="*.txt", loader_cls=TextLoader)
    docs = loader.load()
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    split_docs = splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(split_docs, embeddings)
    db.save_local(VECTOR_DIR)
    return db
