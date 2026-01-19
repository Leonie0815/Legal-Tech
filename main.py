import os
from dotenv import load_dotenv
import streamlit as st

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# 1. API Key laden
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Frontend
st.set_page_config(page_title="Anti-Bot", page_icon="😁")
st.title("👌Anti-Bot💀")

user_input = st.text_area("Was willst du?", height=300)


# Funktionalität
def answer(question):
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=api_key)
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "Antworte in maximal 6 Sätzen. \n"
                   "stelle die Frage die dir gestellt wird in Frage \n"
                   "teile dem Fragesteller mit, dass er die Frage auch besser hätte formulieren können \n"
                   "beantworte die Frage sehr lustlos und uninspiriert \n"
                   "animiere abschließend den Fragesteller auf herablassende Art und Weise dazu nochmal zu fragen"),
        ("user", "{text}")
    ])

    chain = prompt_template | llm | StrOutputParser()

    return chain.invoke({"text": question})
    

if st.button("Abschicken 👍"):
    if user_input:
        with st.spinner("Analysiere..."):
            ergebnis = answer(user_input)
            st.markdown(ergebnis)
    else:
        st.warning("Wer nicht fragt bekommt keine Antwort.")







