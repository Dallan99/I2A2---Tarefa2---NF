import os
import re
import pandas as pd
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

load_dotenv()

def criar_agente(caminho_csv: str):
    # 1) Carrega o arquivo (CSV ou Excel)
    if caminho_csv.lower().endswith(('.xls', '.xlsx')):
        df = pd.read_excel(caminho_csv, engine="xlrd")
    else:
        df = pd.read_csv(
            caminho_csv,
            sep=';',
            encoding='latin-1',
            engine='python',
            on_bad_lines='warn'
        )

    # Armazena a lista de colunas para passar ao prompt
    colunas = df.columns.tolist()
    colunas_str = ", ".join(repr(c) for c in colunas)

    # 2) Cria o LLM
    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=0,
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )

    def run_query(pergunta: str) -> str:
        # ---- passo 1: gerar código pandas (com as colunas explícitas) ----
        prompt_code = f"""
O DataFrame `df` tem estas colunas: {colunas_str}

Você é um gerador de **snippet** Python com pandas.  
Receba a pergunta e **retorne somente** o código Python puro, sem comentários nem texto adicional, 
usando exatamente as colunas disponíveis acima.

Pergunta: {pergunta}

Saída esperada: apenas código Python válido.
"""
        snippet_msg = llm.predict_messages([HumanMessage(content=prompt_code)])
        snippet = snippet_msg.content.strip()

        # ---- passo 2: executar o snippet ----
        try:
            resultado = eval(snippet, {}, {"df": df})
        except Exception as e:
            return f"Erro ao executar o código gerado:\n  {e}\n\nCódigo:\n{snippet}"

        # ---- passo 3: formatar a resposta em PT-BR ----
        prompt_answer = f"""
Você é um formatador de resultados.  
Recebe o output Python de um pandas (variável `resultado = {resultado!r}`)  
e deve retornar **em Português do Brasil**, iniciando com:
"Os principais destinatários são: ..."  

Apenas retorne essa frase final, sem aspas.
"""
        answer_msg = llm.predict_messages([HumanMessage(content=prompt_answer)])
        return answer_msg.content.strip()

    return run_query
