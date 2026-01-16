# import streamlit as st


# # Seite Konfigurieren

# st.set_page_config(page_title="Erste Schritte Legal Tech", page_icon="⚖️")

# # Titel und Einleitung
# st.title("⚖️ Mein erstes Legal-Tech Tool")
# st.write("Willkommen! Dies ist ein Prototyp für einen AGB-Checker.")

# #test


import streamlit as st
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. API Key aus der .env Datei laden
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

def analyze_agb(agb_text):
    # Modell-Konfiguration (GPT-4o-mini ist schnell und kosteneffizient)
    model = ChatGoogleGenerativeAI(model="gemini-pro",google_api_key=api_key, temperature=0)

    # Der System-Prompt definiert die "Rolle" und das Fachwissen der KI
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "Du bist ein spezialisierter Rechtsanwalt für Verbraucherschutz in Deutschland. "
                   "Analysiere den folgenden AGB-Text auf kritische Klauseln, die für Verbraucher "
                   "nachteilig oder ungewöhnlich sein könnten (z.B. versteckte Kosten, lange Kündigungsfristen, "
                   "automatische Verlängerungen oder Haftungsausschlüsse). "
                   "Antworte strukturiert in Markdown mit: \n"
                   "1. Kurzzusammenfassung\n"
                   "2. Kritische Punkte (mit Begründung)\n"
                   "3. Empfehlung."),
        ("user", "{text}")
    ])

    # Die Chain: Prompt -> KI-Modell -> Output als Text
    chain = prompt_template | model | StrOutputParser()

    # Ausführung der Analyse
    return chain.invoke({"text": agb_text})

# --- Streamlit UI Oberfläche ---

st.set_page_config(page_title="LegalTech AGB-Checker", page_icon="⚖️")

st.title("⚖️ KI AGB-Checker")
st.write("Füge einen AGB-Text ein, um ihn auf verbraucherunfreundliche Klauseln zu prüfen.")


# Textfeld für die Eingabe
user_input = st.text_area("AGB Text hier hineinkopieren:", height=300)

if st.button("Analyse starten"):
    if user_input:
        with st.spinner("Die KI analysiert die Paragrafen... bitte warten."):
            try:
                result = analyze_agb(user_input)
                st.markdown("### Analyse-Ergebnis")
                st.markdown(result)
            except Exception as e:
                st.error(f"Ein Fehler ist aufgetreten: {e}")
    else:
        st.warning("Bitte füge zuerst einen Text ein, den ich prüfen soll.")