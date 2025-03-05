Langgraph

A demonstration project showcasing the use of LangChain and graph-based orchestration for building AI applications. This project combines OpenAI's language models with Tavily's search capabilities to create a powerful workflow system.

Credit where credit is due: This project is based on the work presented in the Deep Learning.ai course titled: 'AI Agents in LangGraph'

## About This Project

This application demonstrates:
- Graph-based workflow orchestration using LangChain
- Integration with OpenAI's language models
- Tavily search integration for real-time information retrieval
- Environment management and configuration best practices

## Development Setup

1.  Create and activate a virtual environment
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2.  Install the dependencies
    ```bash
    pip install -U openai
    # for tavily search
    pip install -U tavily-python
    pip install -U langchain-openai
    pip install -U langchain_community
    ```

3.  Configure environment variables
    ```bash
    cp env.example .env
    ```

    Add your OPENAI_API_KEY to the `.env`
    
    Add your TAVILY_API_KEY to the `.env`


## Run the application
```bash
python app.py
```

## Key Components

- **LangChain Integration**: Utilizes LangChain's framework for composing AI applications
- **OpenAI Models**: Leverages OpenAI's language models for natural language processing
- **Tavily Search**: Incorporates Tavily's search capabilities for enhanced information retrieval
- **Graph-based Architecture**: Uses directed graphs for workflow management and execution

