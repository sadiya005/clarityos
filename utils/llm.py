from groq import Groq
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    api_key = st.secrets["GROQ_API_KEY"]

client = Groq(
    api_key=api_key
)

MODEL = "llama-3.3-70b-versatile"


def ask_llm(prompt):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content