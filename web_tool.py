
import requests

def search_web(query: str) -> str:
    try:
        url = f"http://your_oracle_ip:8000/search?q={query}"
        res = requests.get(url)
        return res.text if res.ok else "❌ Failed to fetch results."
    except Exception as e:
        return f"❌ Error: {str(e)}"
