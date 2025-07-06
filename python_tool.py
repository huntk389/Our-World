
import io
from contextlib import redirect_stdout

def run_python_code(code: str) -> str:
    buffer = io.StringIO()
    try:
        with redirect_stdout(buffer):
            exec(code, {})
        return buffer.getvalue()
    except Exception as e:
        return f"❌ Error: {str(e)}"
