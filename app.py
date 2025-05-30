import streamlit as st
from agente import criar_agente

st.set_page_config(page_title="Agente Inteligente para Notas Fiscais - Jan/2024", layout="wide")

st.title("🤖 Agente Inteligente para Notas Fiscais - Jan/2024")

st.markdown("💬 *Faça uma pergunta sobre o arquivo CSV (pressione Enter para enviar)*")

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
