
from vector_store import get_vectorstore

def get_context(query: str) -> str:
    try:
        db = get_vectorstore()
        docs = db.similarity_search(query, k=4)
        return "\n".join([doc.page_content for doc in docs])
    except Exception:
        return ""
