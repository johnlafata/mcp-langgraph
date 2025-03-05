# reference: https://modelcontextprotocol.io/quickstart/client

import asyncio
from typing import Optional
from contextlib import AsyncExitStack

from mcp import ClientSession, StdioServerParameters
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import AnyMessage, SystemMessage, AIMessage, HumanMessage, ToolMessage

from langchain_mcp_adapters.client import MultiServerMCPClient

from mcp.client.stdio import stdio_client

# needed?   
# from anthropic import Anthropic

from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv

_ = load_dotenv()  # load environment variables from .env

class MCPClient:
    def __init__(self, model):
        # Initialize session and client objects
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()
        self.model=model

    async def connect_to_server(self, server_script_path: str):
        """Connect to an MCP server
        Args:
            server_script_path: Path to the server script (.py or .js)
        """
        is_python = server_script_path.endswith('.py')
        is_js = server_script_path.endswith('.js')
        if not (is_python or is_js):
            raise ValueError("Server script must be a .py or .js file")

        command = "python" if is_python else "node"
        server_params = StdioServerParameters(
            command=command,
            args=[server_script_path],
            env=None
        )

        stdio_transport = await self.exit_stack.enter_async_context(stdio_client(server_params))
        self.stdio, self.write = stdio_transport
        self.session = await self.exit_stack.enter_async_context(ClientSession(self.stdio, self.write))

        await self.session.initialize()

        # List available tools
        response = await self.session.list_tools()
        tools = response.tools
        print("\nConnected to server with tools:", [tool.name for tool in tools])

    async def process_query(self, query: str) -> str:
        """Process a query using model and available tools"""
        messages = [
            {
                "role": "user",
                "content": query
            }
        ]

        response = await self.session.list_tools()
        available_tools = [{
            "name": tool.name,
            "description": tool.description,
            "input_schema": tool.inputSchema
        } for tool in response.tools]

        model_with_tools=self.model.bind_tools(available_tools)

        response=model_with_tools.invoke(messages)

        # print(f"Response: {response}")
        # print (type(response.content))

        if isinstance(response.content, str) and response.content != '':
            return response.content

        final_text=[]
        assistant_message_content=[]
        tool_results=[]
        for t in response.tool_calls:
            tool_name=t['name']
            tool_args=t['args']
            print(f"Calling: {tool_name}")
            selected_tool=None
            for tool in available_tools:
                if tool['name']==tool_name:
                    selected_tool=tool
            if selected_tool == None:      # check for bad tool name from LLM
                print("\n ....suggested tool not bound, trying without tools....")
                # result = "suggested tool not bound"  # instruct LLM to retry if bad
                # try to evaluate without tools
                response=self.model.invoke(messages)
                # print("after attept with not tools")
                # print(f"Response: {response}")

                final_text.append(response.content)
            else:
                assistant_message_content.append(t)
                messages.append({
                    "role": "assistant",
                    "content": assistant_message_content
                })

                # # Execute tool call
                # result = available_tools[t['name']].invoke(t['args'])
                result = await self.session.call_tool(tool_name, tool_args)
                # tool_results.append(ToolMessage(tool_call_id=t['id'], name=tool_name, content=str(result)))
                for content in result.content:
                    if content.type == 'text':
                        final_text.append(content.text)
                        assistant_message_content.append(content)
                    elif content.type == 'tool_use':
                        tool_name = content.name
                        tool_args = content.input

                        # Execute tool call
                        result = await self.session.call_tool(tool_name, tool_args)
                        tool_results.append({"call": tool_name, "result": result})
                        final_text.append(f"[Calling tool {tool_name} with args {tool_args}]")

                        assistant_message_content.append(content)
                        messages.append({
                            "role": "assistant",
                            "content": assistant_message_content
                        })
                        messages.append({
                            "role": "user",
                            "content": [
                                {
                                    "type": "tool_result",
                                    "tool_use_id": content.id,
                                    "content": result.content
                                }
                            ]
                        })

                        response=model_with_tools.invoke(messages)
                        # print(response.content[0].text)
                        final_text.append(response.content[0].text)
            
                # print(f"Result.content: {result.content}")
                # # print(f"Result.content: {result.content}")
                # final_text.append(str(result.content))
        # print(messages[-1])
        return "\n".join(final_text)

        # print("**************")
        # print (response)
        # return response


    async def chat_loop(self):
        """Run an interactive chat loop"""
        print("\nMCP Client Started!")
        print("Type your queries or 'quit' to exit.")

        while True:
            try:
                query = input("\nQuery: ").strip()

                if query.lower() == 'quit':
                    break

                response = await self.process_query(query)
                print("\n" + response)

            except Exception as e:
                print(f"\nError: {str(e)}")

    async def cleanup(self):
        """Clean up resources"""
        await self.exit_stack.aclose()

async def main():
    if len(sys.argv) < 2:
        print("Usage: python client.py <path_to_server_script>")
        sys.exit(1)

    client = MCPClient()
    try:
        await client.connect_to_server(sys.argv[1])
        await client.chat_loop()
    finally:
        await client.cleanup()

if __name__ == "__main__":
    import sys
    asyncio.run(main())