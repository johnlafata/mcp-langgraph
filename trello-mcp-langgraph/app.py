import os
from rich.console import Console
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage, SystemMessage


console = Console()

# Works with any tool capable LLM
# llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")
# llm = ChatOpenAI(model="gpt-4o")
llm = ChatOllama(model="llama3.2:latest")


from agent import Agent

system_message = "You are a helpful assistant. Use available tools to assist the user."
my_agent = Agent(model=llm, system=system_message)


def amain() -> None:

    key=os.getenv('TRELLO_API_KEY')
    token=os.getenv('TRELLO_ACCOUNT_TOKEN')
    initial_input = [HumanMessage(content=f"can you list the trello boards using this key {key} and token {token}")]
    
    # Invoke the graph with initial messages
    result= my_agent.invoke(initial_input)
    last_messages=result.get("messages")[-1]
    print(last_messages.get("messages")[-1].content)

def main() -> None:
    amain()

if __name__ == "__main__":
    main()