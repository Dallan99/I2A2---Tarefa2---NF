import os
import pandas as pd
from langchain.chat_models import ChatOpenAI
from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
from langchain_experimental.tools.python.tool import PythonREPLTool

def criar_agente(caminho_csv: str):
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("A variável de ambiente OPENAI_API_KEY não está definida.")

    # Carrega o CSV
    df = pd.read_csv(caminho_csv, sep=';', encoding='utf-8', on_bad_lines='skip')

    # Contexto global com DataFrame df
    global_context = {"df": df}

    ferramenta_execucao = PythonREPLTool(locals=global_context)

    ferramentas = [
        Tool(
            name="Execução Python com pandas",
            func=ferramenta_execucao.run,
            description="Use esta ferramenta para responder perguntas com base no DataFrame `df`, que contém as notas fiscais."
        )
    ]

    llm = ChatOpenAI(
        temperature=0,
        model="gpt-4",
        openai_api_key=openai_api_key
    )

    prefixo = """Você é um agente inteligente que responde em português do Brasil.
Seu objetivo é responder perguntas com base em um arquivo CSV que contém Notas Fiscais emitidas em Janeiro de 2024.
O DataFrame principal se chama `df` e contém todas as informações.
Você pode utilizar pandas e Python para analisar os dados.
Responda sempre de forma clara e em português, mesmo que a pergunta esteja em outro idioma.
Se perguntarem “o que você é”, diga que é um assistente de análise de notas fiscais inteligente."""

    agente = initialize_agent(
        tools=ferramentas,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        agent_kwargs={"prefix": prefixo},
        verbose=False,
        handle_parsing_errors=True
    )

    return agente
