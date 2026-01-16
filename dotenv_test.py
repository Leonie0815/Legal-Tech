import os
from dotenv import load_dotenv
from google import genai
import streamlit as st

# 1. API Key laden from .env file (best practice for not showing key publicly)
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")




st.set_page_config(page_title="mcBot", page_icon="😁")

st.title("👌TestBot💀")

user_input = st.text_area("Wie kann ich dir helfen?", height=300)

if st.button("Abschicken 👍"):
    # 2. Client initialisieren
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=user_input
    )
    output = st.write(response.text)







