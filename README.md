This library a tutorial to introduce the lightweight wrapper using [Anthropic Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) tools with [LangChain](https://github.com/langchain-ai/langchain) and [LangGraph](https://github.com/langchain-ai/langgraph).

The tutorial progresses in phases, starting with a simple tool and gradually increasing complexity. 

[First step: exercise a simple MCP server to connect to Trello](./trello-mcp/README.md)
This is a simple implementation showcasing the integration of Trello with AI capabilities using the Anthropic Model Context Protocol (MCP). This project demonstrates how to build AI-enhanced Trello workflows using LangChain and the OpenAI API.

[Second step: develop a sample langgraph program](./langgraph/README.md) 
This is a simple langgraph program that uses Tavily search tools.    This program uses openai format tools to search for information on the web.  The program is a simple example of how to use langgraph.

[Third step: develop a sample langgraph program that uses the MCP server to connect to Trello](./trello-mcp-langgraph/README.md)
This example combines the work from the first two steps by updating the langgraph program to use the tools introduced in the MCP server to connect to Trello instead of openai format tools.  

[Fourth step: generalize the langgraph program so that any MCP server might be introduced into a langgraph application](./trello-mcp-generalized-langgraph/README.md)
This example parameterizes the tool specification so that any MCP server might be introduced into a langgraph application.  This is a generalized version of the previous example. 


... more to come...




