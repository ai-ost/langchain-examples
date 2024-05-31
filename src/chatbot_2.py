# import getpass (we use .env file instead)
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage

# load environment variables
load_dotenv()

# the model
model = ChatOpenAI(model="gpt-3.5-turbo")

# invoke the model
result = model.invoke(
    [
        HumanMessage(content="Hi! I'm Bob"),
        AIMessage(content="Hello Bob! How can I assist you today?"),
        HumanMessage(content="What's my name?"),
    ]
)

# print the result
print(result.content)

# Your name is Bob.
