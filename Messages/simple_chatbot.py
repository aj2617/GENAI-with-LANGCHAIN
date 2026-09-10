# from langchain_groq import ChatGroq
# from dotenv import load_dotenv
# import streamlit as st
# load_dotenv()

# model=ChatGroq(model='openai/gpt-oss-120b')

# while True:
#     user_input = input('You : ')
    
#     if user_input == 'exit':
#         break
#     res = model.invoke(user_input)
#     print('AI : ',res.content)
    
    
from langchain_groq import ChatGroq
from dotenv import load_dotenv 
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage


load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

chat_history = [ SystemMessage(content="You are a helpful assistant. Always Answer in a short paragraph(1-2 Sentence)")]

#chatbot 
while True:
    user_input = input('You: ')

    if user_input.strip().lower() == 'exit':
        break

    chat_history.append(HumanMessage(content=user_input))

    result = model.invoke(chat_history)

    chat_history.append(AIMessage(content=result.content))
    
    print("AI:", result.content)

print("Printing chat history:", chat_history)
