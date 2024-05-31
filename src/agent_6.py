# import getpass (we use .env file instead)
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.tools.retriever import create_retriever_tool
from langgraph.prebuilt import chat_agent_executor

# load environment variables
load_dotenv()

# search tool
search = TavilySearchResults(max_results=2)

# load the document
loader = WebBaseLoader("https://docs.smith.langchain.com/overview")
docs = loader.load()

# split the document
documents = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=200
).split_documents(docs)

# vectorize the document
vector = FAISS.from_documents(documents, OpenAIEmbeddings())

# get a retriever
retriever = vector.as_retriever()

# create retriever tool
retriever_tool = create_retriever_tool(
    retriever,
    "langsmith_search",
    "Search for information about LangSmith. For any questions about LangSmith, you must use this tool!",
)

# list of available tools
tools = [search, retriever_tool]

# the model
model = ChatOpenAI(model="gpt-3.5-turbo")

# create agent with model and tools
agent_executor = chat_agent_executor.create_tool_calling_executor(model, tools)

# invoke the agent
response = agent_executor.invoke(
    {"messages": [HumanMessage(content="how can langsmith help with testing?")]}
)

# print the response
print(response["messages"])

# [
#     HumanMessage(content='how can langsmith help with testing?', id='04f4fe8f-391a-427c-88af-1fa064db304c'),
#     AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_FNIgdO97wo51sKx3XZOGLHqT', 'function': {'arguments': '{\n  "query": "how can LangSmith help with testing"\n}', 'name': 'langsmith_search'}, 'type': 'function'}]}, response_metadata={'token_usage': {'completion_tokens': 22, 'prompt_tokens': 135, 'total_tokens': 157}, 'model_name': 'gpt-3.5-turbo', 'system_fingerprint': None, 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-51f6ea92-84e1-43a5-b1f2-bc0c12d8613f-0', tool_calls=[{'name': 'langsmith_search', 'args': {'query': 'how can LangSmith help with testing'}, 'id': 'call_FNIgdO97wo51sKx3XZOGLHqT'}]),
#     ToolMessage(content="Getting started with LangSmith...", name='langsmith_search', id='f286c7e7-6514-4621-ac60-e4079b37ebe2', tool_call_id='call_FNIgdO97wo51sKx3XZOGLHqT'),
#     AIMessage(content="LangSmith is a platform that..", response_metadata={'token_usage': {'completion_tokens': 200, 'prompt_tokens': 782, 'total_tokens': 982}, 'model_name': 'gpt-3.5-turbo', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None}, id='run-4b80db7e-9a26-4043-8b6b-922f847f9c80-0')
# ]
