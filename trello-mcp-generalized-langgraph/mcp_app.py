# credits: https://github.com/paulrobello/mcp_langgraph_tools/blob/main/src/mcp_langgraph_tools/__main__.py

import asyncio
import os

from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

# Works with any tool capable LLM
llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")
# llm = ChatOpenAI(model="gpt-4o")
# llm = ChatOllama(model="llama3.2:latest")

from langchain_core.messages import AnyMessage, SystemMessage, AIMessage, HumanMessage, ToolMessage

from mcp_client import MCPClient

async def amain() -> None:

    client = MCPClient(model=llm)
    try:
        await client.connect_to_server("trello-server.py")
        key=os.getenv('TRELLO_API_KEY')
        token=os.getenv('TRELLO_ACCOUNT_TOKEN')
        query=f"can you list the trello boards using this key {key} and token {token}"

        response = await client.process_query(query)
        print("\n" + response)

    finally:
        await client.cleanup()    

def main() -> None:
    asyncio.run(amain())

if __name__ == "__main__":
    import sys
    main()