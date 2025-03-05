# trello-mcp-langgraph

This folder contains the implementation of the Trello MCP Server that showcases the integration of Trello with AI capabilities using the Anthropic Model Context Protocol (MCP) and Langgrqph.

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

