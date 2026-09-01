from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(model= "openai/gpt-oss-120b")
result = llm.invoke("What is 2+2 ")
result1 = llm.invoke("Write about Bangladesh ")

print(result.content)

print(result1.content)