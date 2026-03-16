import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq

def get_llm(provider="gemini"):
    if provider == "gemini":
        return ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            google_api_key=os.getenv("GEMINI_API_KEY")
        )
    elif provider == "groq":
        return ChatGroq(
            model="mixtral-8x7b-32768",
            api_key=os.getenv("GROQ_API_KEY")
        )
