## Installation

This code expands on the previous work to include a generalized langgraph mcp client (which accepts an mcp server) that can be used with any llm. 

Possible Future work:
- expand the mcp server to be a list of mcp servers
- allow additional system prompts for every model invocation

modified mcp client based on: 
    https://modelcontextprotocol.io/quickstart/client 



## Development Setup

1.  Create and activate a virtual environment
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2.  Install the dependencies
    ```bash
    pip install -U openai
    pip install -U langchain_community
    pip install -U mcp
    pip install -U langgraph
    pip install -U python-dotenv
    ```

    Depending on the llm you want to use, you can install the following:
    ```
    pip install -U langchain-openai
    pip install -U langchain-ollama
    pip install -U langchain-anthropic
    ```

3.  Configure environment variables
    ```bash
    cp env.example .env
    ```

    if you will use the openai llm,
        Add your OPENAI_API_KEY  to the `.env`

    if you will use the anthropic llm,
        Add your ANTHROPIC_API_KEY  to the `.env`

    ADD your TRELLO_API_KEY and TRELLO_ACCOUNT_TOKEN to the `.env`


## Run the application
```bash
python app.py
```

## examples of other mcp clients
- https://github.com/paulrobello/mcp_langgraph_tools
- https://github.com/ellieli0630/langgraph-mcp-agent-twitter/blob/main/agent.py
- https://www.pulsemcp.com/clients 
- https://mcp.so/clients 
example mcp client
- https://github.com/rakesh-eltropy/mcp-client
