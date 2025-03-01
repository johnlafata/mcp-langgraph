# Create server parameters for stdio connection
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent

## added to get OPENAI_API_KEY from .env
import os
from dotenv import load_dotenv
load_dotenv()

import logging
logging.basicConfig(level=logging.INFO)

from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, ToolMessage
model = ChatOpenAI(model="gpt-4o")

async def main():
    async with MultiServerMCPClient() as client:
        await client.connect_to_server(
            "math",
            command="python",
            # Make sure to update to the full absolute path to your math_server.py file
            args=["math_server.py"],
        )
        await client.connect_to_server(
            "weather",
            command="python",
            # Make sure to update to the full absolute path to your weather_server.py file
            args=["weather_server.py"],
        )
        await client.connect_to_server(
            "trello",
            command="python",
            # Make sure to update to the full absolute path to your weather_server.py file
            args=["trello-server.py"],
        )
        agent = create_react_agent(model, client.get_tools())
        # math_response = await agent.ainvoke({"messages": "what's (3 + 5) x 12?"})
        # print(math_response)
        # weather_response = await agent.ainvoke({"messages": "what is the weather in nyc?"})
        # print(weather_response)
        key=os.getenv('TRELLO_API_KEY')
        logging.debug(f'key: {key}')
        token=os.getenv('TRELLO_ACCOUNT_TOKEN')
        logging.debug(f'token: {token}')
        trello_response = await agent.ainvoke({"messages": f"can you list the trello boards using this {key} and {token}"})
        response_object=trello_response.get("messages")[-1].content
        print(response_object)
        trello_response = await agent.ainvoke({"messages": f"Now show me the list names on the board using the id of the board with the name 'garage' using same this {key} and {token}"})
        response_object=trello_response.get("messages")[-1].content
        print(response_object)        
        trello_response = await agent.ainvoke({"messages": f"Show me the cards on the list named 'To do' on the trello board named 'garage'using the  {key} and {token}"})
        response_object=trello_response.get("messages")[-1].content
        print(response_object)        

import asyncio
asyncio.run(main())