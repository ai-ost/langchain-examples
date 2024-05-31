# import getpass (we use .env file instead)
from dotenv import load_dotenv
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

# invoke the search tool
result = search.invoke("what is the weather in SF")

# print the result
print(result)

# [{'url': 'https://www.weatherapi.com/', 'content': "{'location': {'name': 'San Francisco', 'region': 'California', 'country': 'United States of America', 'lat': 37.78, 'lon': -122.42, 'tz_id': 'America/Los_Angeles', 'localtime_epoch': 1717149313, 'localtime': '2024-05-31 2:55'}, 'current': {'last_updated_epoch': 1717148700, 'last_updated': '2024-05-31 02:45', 'temp_c': 8.0, 'temp_f': 46.4, 'is_day': 0, 'condition': {'text': 'Mist', 'icon': '//cdn.weatherapi.com/weather/64x64/night/143.png', 'code': 1030}, 'wind_mph': 2.2, 'wind_kph': 3.6, 'wind_degree': 10, 'wind_dir': 'N', 'pressure_mb': 1012.0, 'pressure_in': 29.89, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 100, 'cloud': 0, 'feelslike_c': 6.4, 'feelslike_f': 43.6, 'windchill_c': 10.8, 'windchill_f': 51.5, 'heatindex_c': 11.7, 'heatindex_f': 53.1, 'dewpoint_c': 8.3, 'dewpoint_f': 46.9, 'vis_km': 8.0, 'vis_miles': 4.0, 'uv': 1.0, 'gust_mph': 9.9, 'gust_kph': 15.9}}"}, {'url': 'https://weatherspark.com/h/m/557/2024/5/Historical-Weather-in-May-2024-in-San-Francisco-California-United-States', 'content': 'San Francisco Temperature History May 2024. The daily range of reported temperatures (gray bars) and 24-hour highs (red ticks) and lows (blue ticks), placed over the daily average high (faint red line) and low (faint blue line) temperature, with 25th to 75th and 10th to 90th percentile bands.'}]


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

# invoke the retriever
result = retriever.invoke("how to upload a dataset")

# print the result
print(result)

# x= [Document(page_content='content...', metadata={
#         'source': 'https://docs.smith.langchain.com/overview',
#         'title': 'title...',
#         'description': 'description...',
#         'language': 'en'
#     }), Document(page_content='more content...', metadata={
#         'source': 'https://docs.smith.langchain.com/overview',
#         'title': 'title...',
#         'description': 'description...',
#         'language': 'en'
#     }),...]

# create retriever tool
retriever_tool = create_retriever_tool(
    retriever,
    "langsmith_search",
    "Search for information about LangSmith. For any questions about LangSmith, you must use this tool!",
)

# list of available tools
tools = [search, retriever_tool]
