from langgraph.graph import StateGraph, END
from langchain_core.messages import  AIMessage

# for mcp tools
from langgraph.prebuilt import create_react_agent
from langchain_mcp_adapters.client import MultiServerMCPClient

from dotenv import load_dotenv
_ = load_dotenv()

from state import AgentState
import asyncio

class Agent:
    def __init__(self, model, system=""):
        self.model = model
        self.system = system
        self.create_mcp_graph()

    ## main entry point to request an AI completion
    def invoke(self, messages):
        response =asyncio.run(self.react_graph.ainvoke({"messages": messages}))
        return response

    
    def create_mcp_graph(self):
        graph = StateGraph(AgentState)
        graph.add_node("llm", self.react_graph_invoke)
        graph.set_entry_point("llm")
        graph.add_edge("llm", END)
        self.react_graph = graph.compile()
 
    # this is the function that is called by the function called by the graph - it includes binding to mcp functions */
    async def make_mcp_agent_call(self,messages):
        async with MultiServerMCPClient() as client:
            await client.connect_to_server(
                "trello",
                command="python",
                # Make sure to update to the full absolute path to your trello-server.py file
                args=["trello-server.py"],
            )
            agent = create_react_agent(self.model, client.get_tools())
            response = await agent.ainvoke({"messages": messages})
            return response

    # ** this is the function that is called by the graph */
    def react_graph_invoke(self, state: AgentState):
        new_messages = []
        messages = state["messages"]

        try:
            result= asyncio.run( self.make_mcp_agent_call(messages) )
            # for m in result["messages"]:
            #     m.pretty_print()    
            new_messages.append( result )
        
        except Exception as e:
            print ("~~~~~~~~~~ throwing exception ~~~~~~~~~~")
            result=f"Error executing tool: {str(e)}"
            new_messages.append(
                AIMessage(
                    content=result
                )
            )
        return {"messages": state["messages"] + new_messages}     

