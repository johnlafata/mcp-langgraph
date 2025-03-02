pip install langchain-mcp-adapters requests langgraph langchain-openai python-dotenv 


## Installation

```bash
alias python='pyenv exec python'
alias pip='pyenv exec pip'
python -m venv venv
source venv/bin/activate


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

