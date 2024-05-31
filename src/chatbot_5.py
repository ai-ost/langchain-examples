# import getpass (we use .env file instead)
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

# load environment variables
load_dotenv()

# the model
model = ChatOpenAI(model="gpt-3.5-turbo")

# the prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Answer all questions to the best of your ability.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

# the chain
chain = prompt | model

# the message store
store = {}


# function to fetch the message history for a specific session
def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]


# the runnable with chain this time
with_message_history = RunnableWithMessageHistory(chain, get_session_history)

# runnable configuration
config = {"configurable": {"session_id": "abc5"}}

# first invocation
response = with_message_history.invoke(
    [HumanMessage(content="Hi! I'm Jim")],
    config=config,
)

# print the result
print(response.content)

# Hello, Jim! How can I assist you today?

# second invocation
response = with_message_history.invoke(
    [HumanMessage(content="What's my name?")],
    config=config,
)

# print the result
print(response.content)

# Your name is Jim. How can I assist you further, Jim?