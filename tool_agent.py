
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI
from file_tool import write_file, append_file, read_file

def run_tool_agent(task: str) -> str:
    tools = [
        Tool(name="write_file", func=lambda x: write_file(x.split("|")[0], x.split("|")[1]), description="Write a new file. Use format: filename|content"),
        Tool(name="append_file", func=lambda x: append_file(x.split("|")[0], x.split("|")[1]), description="Append content to a file. Use format: filename|content"),
        Tool(name="read_file", func=read_file, description="Read a file. Input is filename only.")
    ]

    llm = ChatOpenAI(temperature=0, model="gpt-4")
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)
    return agent.run(task)
