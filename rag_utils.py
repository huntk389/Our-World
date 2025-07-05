from vector_store import get_vectorstore
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

def get_context(question: str) -> str:
    vectordb = get_vectorstore()
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})
    qa_chain = RetrievalQA.from_chain_type(llm=ChatOpenAI(), retriever=retriever)
    return qa_chain.run(question)