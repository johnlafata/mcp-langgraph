from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import AnyMessage, SystemMessage, HumanMessage, ToolMessage

from agent import Agent

tool = TavilySearchResults(max_results=4) #increased number of results
print(type(tool))
print(tool.name)

tools=[]
tools.append(tool)

prompt = """You are a smart research assistant. Use the search engine to look up information. \
You are allowed to make multiple calls (either together or in sequence). \
Only look up information when you are sure of what you want. \
If you need to look up some information before asking a follow up question, you are allowed to do that!
"""

model = ChatOpenAI(model="gpt-4o")  #reduce inference cost
abot = Agent(model, tools, system=prompt)

if __name__ == "__main__":
    messages = [HumanMessage(content="What is the weather in sf?")]
    result = abot.graph.invoke({"messages": messages})
    print("--- ")
    print(result)
    print("--- ")
    print (result.get("messages")[-1].content)