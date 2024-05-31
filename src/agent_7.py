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
    {"messages": [HumanMessage(content="whats the weather in sf?")]}
)

# print the response
print(response["messages"])

# [
#     HumanMessage(content='whats the weather in sf?', id='e6b716e6-da57-41de-a227-fee281fda588'),
#     AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_TGDKm0saxuGKJD5OYOXWRvLe', 'function': {'arguments': '{\n  "query": "current weather in San Francisco"\n}', 'name': 'tavily_search_results_json'}, 'type': 'function'}]}, response_metadata={'token_usage': {'completion_tokens': 23, 'prompt_tokens': 134, 'total_tokens': 157}, 'model_name': 'gpt-3.5-turbo', 'system_fingerprint': None, 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-fd7d5854-2eab-4fca-ad9e-b3de8d587614-0', tool_calls=[{'name': 'tavily_search_results_json', 'args': {'query': 'current weather in San Francisco'}, 'id': 'call_TGDKm0saxuGKJD5OYOXWRvLe'}]),
#     ToolMessage(content='[{"url": "https://www.weatherapi.com/", "content": "{\'location\': {\'name\': \'San Francisco\', \'region\': \'California\', \'country\': \'United States of America\', \'lat\': 37.78, \'lon\': -122.42, \'tz_id\': \'America/Los_Angeles\', \'localtime_epoch\': 1714426800, \'localtime\': \'2024-04-29 14:40\'}, \'current\': {\'last_updated_epoch\': 1714426200, \'last_updated\': \'2024-04-29 14:30\', \'temp_c\': 17.8, \'temp_f\': 64.0, \'is_day\': 1, \'condition\': {\'text\': \'Sunny\', \'icon\': \'//cdn.weatherapi.com/weather/64x64/day/113.png\', \'code\': 1000}, \'wind_mph\': 23.0, \'wind_kph\': 37.1, \'wind_degree\': 290, \'wind_dir\': \'WNW\', \'pressure_mb\': 1019.0, \'pressure_in\': 30.09, \'precip_mm\': 0.0, \'precip_in\': 0.0, \'humidity\': 50, \'cloud\': 0, \'feelslike_c\': 17.8, \'feelslike_f\': 64.0, \'vis_km\': 16.0, \'vis_miles\': 9.0, \'uv\': 5.0, \'gust_mph\': 27.5, \'gust_kph\': 44.3}}"}, {"url": "https://www.wunderground.com/hourly/us/ca/san-francisco/94125/date/2024-4-29", "content": "Current Weather for Popular Cities . San Francisco, CA warning 59 \\u00b0 F Mostly Cloudy; Manhattan, NY 56 \\u00b0 F Fair; Schiller Park, IL (60176) warning 58 \\u00b0 F Mostly Cloudy; Boston, MA 52 \\u00b0 F Sunny ..."}]', name='tavily_search_results_json', id='aa0d8c3d-23b5-425a-ad05-3c174fc04892', tool_call_id='call_TGDKm0saxuGKJD5OYOXWRvLe'),
#     AIMessage(content='The current weather in San Francisco, California is sunny with a temperature of 64.0°F (17.8°C). The wind is coming from the WNW at a speed of 23.0 mph. The humidity level is at 50%. There is no precipitation and the cloud cover is 0%. The visibility is 16.0 km. The UV index is 5.0. Please note that this information is as of 14:30 on April 29, 2024, according to [Weather API](https://www.weatherapi.com/).', response_metadata={'token_usage': {'completion_tokens': 117, 'prompt_tokens': 620, 'total_tokens': 737}, 'model_name': 'gpt-3.5-turbo', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None}, id='run-2359b41b-cab6-40c3-b6d9-7bdf7195a601-0')
# ]
