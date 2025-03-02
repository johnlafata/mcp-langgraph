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
    pip install -U openai
    # for tavily search
    pip install -U tavily-python
    pip install -U langchain-openai
    pip install -U langchain_community

3.  Configure environment variables
    ```bash
    cp env.example .env
    ```
    Add your OPENAI_API_KEY to the `.env`
    ADD your TIVOLI_API_KEY to the `.env`

