import streamlit as st
import pandas as pd
from agente import criar_agente
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Agente Inteligente para NF", layout="wide")

st.title("🤖 Agente de Notas Fiscais - Janeiro/2024")

st.markdown("""
Faça perguntas como:
- Qual o valor total das notas?
- Qual UF mais emitiu notas?
- Quais os principais destinatários?
""")

# Escolha aqui qual arquivo usar: cabeçalho (CSV) ou itens (XLS)
CSV_PATH = "202401_NFs_Itens.xls"

# Carrega um exemplo rápido para mostrar (opcional)
with st.expander("📂 Preview do DataFrame"):
    if CSV_PATH.lower().endswith(('.xls', '.xlsx')):
        sample = pd.read_excel(CSV_PATH, engine="xlrd")
    else:
        sample = pd.read_csv(
            CSV_PATH, sep=';', encoding='latin-1', engine='python', on_bad_lines='warn'
        )
    st.dataframe(sample.head())

# Cria a função de consulta
run_query = criar_agente(CSV_PATH)

pergunta = st.text_input("Digite sua pergunta aqui:", "")
if pergunta:
    with st.spinner("Processando…"):
        resposta = run_query(pergunta)
    st.markdown("### 📄 Resposta:")
    st.write(resposta)
