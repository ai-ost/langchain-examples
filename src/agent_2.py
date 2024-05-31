# import getpass (we use .env file instead)
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.tools.retriever import create_retriever_tool

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

# invoke the model
response = model.invoke([HumanMessage(content="hi!")])

# print the response
print(response.content)

# Hello! How can I assist you today?
