import streamlit as st
from agente import criar_agente
import os

api_key = os.getenv("OPENAI_API_KEY")




st.set_page_config(page_title="Agente Inteligente para Notas Fiscais - Jan/2024", layout="wide")
st.image("images/logo.jpg", width=100)
st.title("🤖 Agente Inteligente para Notas Fiscais - Jan/2024")

st.markdown("""
💬 *Faça uma pergunta sobre o arquivo CSV (pressione Enter para enviar)*

**Exemplos de perguntas:**
- 🧾 Qual o valor total das notas fiscais?
- 📍 Quais estados mais emitiram notas?
- 👤 Quais os principais destinatários?
""")


try:
    agente = criar_agente("202401_NFs_Cabecalho.csv")

    pergunta = st.text_input("", placeholder="Digite sua pergunta aqui...")

    if pergunta:
        with st.spinner("🔎 Consultando os dados..."):
            resposta = agente.run(pergunta)
            st.markdown("### 📄 Resposta:")
            st.write(resposta)

except ValueError as e:
    st.error(str(e))
