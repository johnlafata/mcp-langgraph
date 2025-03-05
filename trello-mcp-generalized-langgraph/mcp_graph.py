from dotenv import load_dotenv
_ = load_dotenv()

import os
import asyncio
from langgraph.graph import MessagesState
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langgraph.graph import START, StateGraph, END
from langgraph.prebuilt import tools_condition

from state import AgentState
from mcp_graph_node import MCPGraphNode

from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_anthropic import ChatAnthropic

# Works with any tool capable LLM
llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")
# llm = ChatOpenAI(model="gpt-4o")
# llm = ChatOllama(model="llama3.2:latest")

prompt = """You are a smart research assistant. Use the search engine to look up information. \
You are allowed to make multiple calls (either together or in sequence). \
Only look up information when you are sure of what you want. \
If you need to look up some information before asking a follow up question, you are allowed to do that!
"""
system_message = "You are a helpful assistant. Use available tools to assist the user."


def create_mcp_graph():
    graph = StateGraph(AgentState)
    graph.add_node("llm", execute_graph_node_query)
    graph.set_entry_point("llm")
    graph.add_edge("llm", END)
    react_graph = graph.compile()
    return react_graph

trello_graph_node= MCPGraphNode(model=llm, server="trello-server.py")

def execute_graph_node_query(state: AgentState):
    messages = state['messages']
    query=messages[-1].content
    result=trello_graph_node.process_request(query)
    result_message=AIMessage(content=result)
    new_messages=[result_message]    
    return {"messages": state["messages"] + new_messages}     

async def amain() -> None:

    react_graph=create_mcp_graph()

    print("**** First Query:")
    key=os.getenv('TRELLO_API_KEY')
    token=os.getenv('TRELLO_ACCOUNT_TOKEN')
    initial_input = [HumanMessage(content=f"can you list the trello boards using this key {key} and token {token}")]
    response=await react_graph.ainvoke({"messages": initial_input})

    last_message=response.get("messages")[-1]
    print(last_message.content)

    print("**** Second Query:")
    initial_input = [HumanMessage(content=f"Who was the sixth president of the United States?")]

    response=await react_graph.ainvoke({"messages": initial_input})
    last_message=response.get("messages")[-1]
    print(last_message.content)

    # ollama really doesn't like this question, It tries to call the trello functions to answer it
    print("**** Third Query:")
    # initial_input = [HumanMessage(content=f"Why is there air?")]
    # ollama really doesn't like this question, It tries to call the trello functions to answer it
    initial_input = [HumanMessage(content=f"What is a diamond?")]

    response=await react_graph.ainvoke({"messages": initial_input})
    last_message=response.get("messages")[-1]
    print(last_message.content)


def main() -> None:
    asyncio.run(amain())

if __name__ == "__main__":
    import sys
    main()