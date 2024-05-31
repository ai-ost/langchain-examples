# import getpass (we use .env file instead)
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
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
response = agent_executor.invoke({"messages": [HumanMessage(content="hi!")]})

# print the response
print(response["messages"])

# [
#     HumanMessage(content='hi!', id='e93eefa7-5a20-499d-8c14-c716a128d035'),
#     AIMessage(content='Hello! How can I assist you today?', response_metadata={'token_usage': {'completion_tokens': 10, 'prompt_tokens': 129, 'total_tokens': 139}, 'model_name': 'gpt-3.5-turbo', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None}, id='run-5f68818e-14fb-4f51-8817-12ae4578a3f4-0', usage_metadata={'input_tokens': 129, 'output_tokens': 10, 'total_tokens': 139})
# ]
