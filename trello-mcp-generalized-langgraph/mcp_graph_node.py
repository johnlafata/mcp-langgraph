from state import AgentState
import asyncio

from mcp_client import MCPClient
# from mcp_client_anthropic_only import MCPClient

class MCPGraphNode:
    def  __init__(self, model, server="trello-server.py"):
        self.model = model
        self.server = server
        self.client = MCPClient(model)

    def process_request(self, query):
        return asyncio.run( self.aprocess_request(query))

    async def aprocess_request(self, query):
        await self.client.connect_to_server(self.server)
        response=await self.client.process_query(query)
        await self.client.cleanup()
        return response

    async def destroy(self):
        await self.client.cleanup()





    
