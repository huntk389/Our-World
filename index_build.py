import os
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

source_folder = "story"
persist_directory = ".vector"

docs = []
for filename in os.listdir(source_folder):
    if filename.endswith(".txt"):
        loader = TextLoader(os.path.join(source_folder, filename))
        docs.extend(loader.load())

splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=100)
texts = splitter.split_documents(docs)

embedding = OpenAIEmbeddings()
Chroma.from_documents(texts, embedding, persist_directory=persist_directory)
print("Index built.")
