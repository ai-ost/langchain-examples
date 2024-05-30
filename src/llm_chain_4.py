# import getpass (we use .env file instead)
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# load environment variables
load_dotenv()

# the model
model = ChatOpenAI(model="gpt-3.5-turbo")

# the system template
system_template = "Translate the following into {language}:"

# the prompt template
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

# invoke the prompt
result = prompt_template.invoke({"language": "italian", "text": "hi"})

# print the prompt
print(result)

# get messages
messages = result.to_messages()

# print the messages
print(messages)

# [SystemMessage(content='Translate the following into italian:'), HumanMessage(content='hi')]

# the parser
parser = StrOutputParser()

# the chain
chain = prompt_template | model | parser

# invoke the chain
content = chain.invoke({"language": "italian", "text": "hi"})

# print the result
print(content)

# "Ciao!"
