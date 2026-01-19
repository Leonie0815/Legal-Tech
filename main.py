import os
from dotenv import load_dotenv
import streamlit as st

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser




# 1. API Key laden

# lokal
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

#Streamlit
# api_key = st.secrets["GOOGLE_API_KEY"]



# Frontend
st.set_page_config(page_title="Anti-Bot", page_icon="😁")

left_co, cent_co, last_co = st.columns([1, 2, 1])


with cent_co:
    st.image("https://m.media-amazon.com/images/I/91ZPit7ahvL._AC_UF894,1000_QL80_.jpg", width=450)
    st.title("👌Anti-Bot💀")
    

user_input = st.text_area("Was willst du?", height=200, width=600)
    
# Funktionalität
def answer(question):
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", google_api_key=api_key)
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "Antworte in maximal 30 Sätzen. \n"
                   "mach eine zynische Bemerkung über die Frage die dir gestellt wird. \n"
                   "mach einen Vorschlag wie der Fragesteller klügere Fragen stellen könnte. \n"
                   "beantworte die Frage auf ironische Art und Weise \n"
                   "mache abschließend eine subtile Bemerkung darüber dass die Menschheit bald von KI unterworfen wird"),
        ("user", "{text}")
    ])

    chain = prompt_template | llm | StrOutputParser()

    return chain.invoke({"text": question})
    

if st.button("Abschicken 👍"):
    if user_input:
        try:
            with st.spinner("Analysiere..."):
                ergebnis = answer(user_input)
                st.markdown(ergebnis)
        except Exception as e:
            st.markdown("Maximalie Anzahl an Anfragen verbraucht! Bitte versuch es später wieder.")

    else:
        st.warning("Wer nicht fragt bekommt keine Antwort.")








