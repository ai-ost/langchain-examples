# import getpass (we use .env file instead)
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# load environment variables
load_dotenv()

# the model
model = ChatOpenAI(model="gpt-3.5-turbo")

# invoke the model
result = model.invoke([HumanMessage(content="Hi! I'm Bob")])

# print the result
print(result.content)

# Hello Bob! How can I assist you today?

# invoke the model again
result = model.invoke([HumanMessage(content="What's my name?")])

# print the result again
print(result.content)

# I'm sorry, I don't know your name. Can you please tell me?
