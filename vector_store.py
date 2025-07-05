
import os
from pathlib import Path
from langchain_community.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader

VECTOR_DIR = "data/vector_index"
MEMORY_FILE = "data/memory.txt"

def get_vectorstore():
    # Load if index already exists
    if Path(VECTOR_DIR).exists():
        return FAISS.load_local(VECTOR_DIR, OpenAIEmbeddings(), allow_dangerous_deserialization=True)

    # Otherwise rebuild from memory.txt
    if not Path(MEMORY_FILE).exists():
        raise FileNotFoundError(f"Missing context file: {MEMORY_FILE}")

    loader = TextLoader(MEMORY_FILE)
    docs = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    split_docs = text_splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(split_docs, embeddings)
    vectorstore.save_local(VECTOR_DIR)
    return vectorstore
