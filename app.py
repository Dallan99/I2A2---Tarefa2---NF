import os
import streamlit as st
import pandas as pd
from dotenv import load_dotenv
from agente import criar_agente

# --- 1) Carrega a API key: tenta Streamlit Cloud, senão .env local ---
try:
    api_key = st.secrets["OPENAI_API_KEY"]
except Exception:
    load_dotenv()  # só carrega no local
    api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error(
        "🚨 Chave da OpenAI não encontrada!\n\n"
        "Defina OPENAI_API_KEY em st.secrets (Streamlit Cloud) ou no seu arquivo .env (local)."
    )
    st.stop()

# --- 2) Configura a página ---
st.set_page_config(page_title="Agente NF - Janeiro/2024", layout="wide")
st.image("images/logo.jpg", width=100)  
st.title("Agente de Notas Fiscais - Janeiro/2024")

st.markdown("""
Faça perguntas como:
- Qual o valor total das notas?
- Qual UF mais emitiu notas?
- Quais os principais destinatários?
""")

# --- 3) Carrega e mostra um preview do DataFrame ---
CSV_PATH = "202401_NFs_Itens.xls"
with st.expander("📂 Preview do DataFrame"):
    if CSV_PATH.lower().endswith((".xls", ".xlsx")):
        df_preview = pd.read_excel(CSV_PATH, engine="xlrd")
    else:
        df_preview = pd.read_csv(
            CSV_PATH,
            sep=";",
            encoding="latin-1",
            engine="python",
            on_bad_lines="warn"
        )
    st.dataframe(df_preview.head())

# --- 4) Cria o agente passando a chave ---
run_query = criar_agente(CSV_PATH, api_key)

# --- 5) Campo de input e exibição da resposta ---
pergunta = st.text_input("Digite sua pergunta aqui:", "")
if pergunta:
    with st.spinner("Processando…"):
        resposta = run_query(pergunta)
    st.markdown("### 📄 Resposta:")
    st.write(resposta)
