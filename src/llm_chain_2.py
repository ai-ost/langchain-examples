# import getpass (we use .env file instead)
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser

# load environment variables
load_dotenv()

# the model
model = ChatOpenAI(model="gpt-3.5-turbo")

# the messages
messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="hi!"),
]

# the parser
parser = StrOutputParser()

# invoke the model
result = model.invoke(messages)

# invoke the parser
content = parser.invoke(result)

# print the result
print(content)

# "Ciao!"
