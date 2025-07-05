from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

embedding = OpenAIEmbeddings()
retriever = Chroma(persist_directory=".vector", embedding_function=embedding).as_retriever()
