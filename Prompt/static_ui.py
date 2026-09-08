from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
from groq import APIConnectionError
import os

load_dotenv()

st.header("Research Tool")
user_input=st.text_input("Enter your prompt")

if st.button("Summarize"):
    if not os.getenv("GROQ_API_KEY"):
        st.error("Missing GROQ_API_KEY. Add it to a .env file, then restart Streamlit.")
        st.stop()

    #model invoke-> woth user prompt 
    
    try:
        model = ChatGroq(model="openai/gpt-oss-120b")
        result = model.invoke(user_input)
        st.write(result.content)
    except APIConnectionError:
        st.error("Could not connect to Groq. Check network, firewall, VPN, or proxy access to api.groq.com.")

