from langchain.llms import OpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

llm = OpenAI(temperature=0.4)

def get_solyn_response(query, retriever, tools, dev_mode=False):
    memory = ConversationBufferMemory(return_messages=True)
    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory
    )
    response = chain.run(query)
    if dev_mode:
        response = f"[DEV MODE]
{response}"
    return response
