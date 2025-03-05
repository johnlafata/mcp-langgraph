# Trello MCP Server

A lightweight implementation showcasing the integration of Trello with AI capabilities using the Anthropic Model Context Protocol (MCP). This project demonstrates how to build AI-enhanced Trello workflows using LangChain and the OpenAI API.

Key Features:
- MCP integration for AI-powered task management
- LangChain workflow automation
- Trello API integration
- Environment-based configuration

## Development Setup

1.  Create and activate a virtual environment
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2.  Install the dependencies
    ```bash
    pip install langchain-mcp-adapters requests langgraph langchain-openai python-dotenv 
    ```

3.  Configure environment variables
    ```bash
    cp env.example .env
    ```
    Add your OPENAI_API_KEY to the `.env`
    
    ADD your TRELLO_API_KEY and TRELLO_ACCOUNT_TOKEN to the `.env`

## Run the application
```bash
python trello-client.py
```

#### The folder also includes a sample fastapi service that can be use to test the call being served in the mcp server.
```bash
python fastapi-client-api.py
```