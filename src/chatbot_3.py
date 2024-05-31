# import getpass (we use .env file instead)
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

# load environment variables
load_dotenv()

# the model
model = ChatOpenAI(model="gpt-3.5-turbo")

# the message store
store = {}


# function to fetch the message history for a specific session
def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]


# the runnable
with_message_history = RunnableWithMessageHistory(model, get_session_history)

# runnable configuration
config = {"configurable": {"session_id": "abc2"}}

# first invocation
response = with_message_history.invoke(
    [HumanMessage(content="Hi! I'm Bob")],
    config=config,
)

# print the result
print(response.content)

# Hello Bob! How can I assist you today?

# second invocation
response = with_message_history.invoke(
    [HumanMessage(content="What's my name?")],
    config=config,
)

# print the result
print(response.content)

# Your name is Bob.

# change the config to use a different session id
config = {"configurable": {"session_id": "abc3"}}

# third invocation
response = with_message_history.invoke(
    [HumanMessage(content="What's my name?")],
    config=config,
)

# print the result
print(response.content)

# I'm sorry, I do not have the ability to know your name unless you tell me.

# change the config back to use the original session id
config = {"configurable": {"session_id": "abc2"}}

# forth invocation
response = with_message_history.invoke(
    [HumanMessage(content="What's my name?")],
    config=config,
)

# print the result
print(response.content)

# Your name is Bob.
