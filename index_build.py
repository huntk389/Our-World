
import os
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

story_dir = "story"
os.makedirs(story_dir, exist_ok=True)

def build_index():
    loader = TextLoader(os.path.join(story_dir, "memory.txt"))
    docs = loader.load()
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_documents(docs)
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(chunks, embeddings)
    db.save_local("vector_index")

if __name__ == "__main__":
    build_index()
    print("✅ Vector index built.")
