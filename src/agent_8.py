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
from langgraph.checkpoint.sqlite import SqliteSaver

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

# checkpoint in memory
memory = SqliteSaver.from_conn_string(":memory:")

# create agent with model and tools
agent_executor = chat_agent_executor.create_tool_calling_executor(
    model, tools, checkpointer=memory
)

# execution config
config = {"configurable": {"thread_id": "abc123"}}

# first invocation
for chunk in agent_executor.stream(
    {"messages": [HumanMessage(content="hi im bob!")]}, config
):
    print(chunk)
    print("-----")

# {
#     'agent': {
#         'messages': [
#             AIMessage(content='Hello Bob! How can I assist you today?', response_metadata={'token_usage': {'completion_tokens': 11, 'prompt_tokens': 131, 'total_tokens': 142}, 'model_name': 'gpt-3.5-turbo', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None}, id='run-607733e3-4b8d-4137-ae66-8a4b8ccc8d40-0')
#         ]
#     }
# }
# -----

# second invocation
for chunk in agent_executor.stream(
    {"messages": [HumanMessage(content="whats my name?")]}, config
):
    print(chunk)
    print("-----")

# {
#     'agent': {
#         'messages': [
#             AIMessage(content='Your name is Bob. How can I assist you further?', response_metadata={'token_usage': {'completion_tokens': 13, 'prompt_tokens': 154, 'total_tokens': 167}, 'model_name': 'gpt-3.5-turbo', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None}, id='run-e1181ba6-732d-4564-b479-9f1ab6bf01f6-0')
#         ]
#     }
# }
