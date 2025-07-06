
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI
from file_tool import write_file, append_file, read_file
from python_tool import run_python_code
from web_tool import search_web

def run_tool_agent(task: str) -> str:
    tools = [
        Tool(name="write_file", func=lambda x: write_file(x.split("|")[0], x.split("|")[1]), description="Write a file: filename|content"),
        Tool(name="append_file", func=lambda x: append_file(x.split("|")[0], x.split("|")[1]), description="Append to a file: filename|content"),
        Tool(name="read_file", func=read_file, description="Read a file: filename"),
        Tool(name="python", func=run_python_code, description="Execute Python code directly."),
        Tool(name="web_search", func=search_web, description="Search the web for up-to-date information.")
    ]

    llm = ChatOpenAI(temperature=0, model="gpt-4")
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)
    return agent.run(task)
