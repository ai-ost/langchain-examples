# import getpass (we use .env file instead)
from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from typing import List

# load environment variables
load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo")

documents = [
    Document(
        page_content="Dogs are great companions, known for their loyalty and friendliness.",
        metadata={"source": "mammal-pets-doc"},
    ),
    Document(
        page_content="Cats are independent pets that often enjoy their own space.",
        metadata={"source": "mammal-pets-doc"},
    ),
    Document(
        page_content="Goldfish are popular pets for beginners, requiring relatively simple care.",
        metadata={"source": "fish-pets-doc"},
    ),
    Document(
        page_content="Parrots are intelligent birds capable of mimicking human speech.",
        metadata={"source": "bird-pets-doc"},
    ),
    Document(
        page_content="Rabbits are social animals that need plenty of space to hop around.",
        metadata={"source": "mammal-pets-doc"},
    ),
]


# vectorize the document
vectorstore = Chroma.from_documents(
    documents,
    embedding=OpenAIEmbeddings(),
)

# the retriever
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 1},
)

# the template
message = """
Answer this question using the provided context only.

{question}

Context:
{context}
"""

# the prompt
prompt = ChatPromptTemplate.from_messages([("human", message)])

# the chain
rag_chain = {"context": retriever, "question": RunnablePassthrough()} | prompt | model

# invoke the chain
response = rag_chain.invoke("tell me about cats")

# print the response
print(response.content)

# Cats are independent pets that often enjoy their own space.
