from vector_store import get_vectorstore

def get_context(query):
    db = get_vectorstore()
    docs = db.similarity_search(query)
    return "\n".join([d.page_content for d in docs])