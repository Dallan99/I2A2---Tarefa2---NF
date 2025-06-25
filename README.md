# BrainAI – Agente de Notas Fiscais (Janeiro/2024)

Este repositório contém um **agente inteligente** que responde, via navegador, a perguntas em linguagem natural sobre notas fiscais emitidas em janeiro de 2024. O projeto combina:

- **Pandas** para manipulação de DataFrames  
- **LangChain + OpenAI** para geração de trechos de código Python  
- **Streamlit** para interface web interativa  

---

## 📋 Sumário

1. [Visão Geral](#visão-geral)  
2. [Pré-requisitos](#pré-requisitos)  
3. [Clonando o Repositório](#clonando-o-repositório)  
4. [Entrando na Pasta do Projeto](#entrando-na-pasta-do-projeto)  
5. [Criando e Ativando o Ambiente Virtual](#criando-e-ativando-o-ambiente-virtual)  
6. [Instalando Dependências](#instalando-dependências)  
7. [Configurando a API Key da OpenAI](#configurando-a-api-key-da-openai)  
8. [Fonte de Dados (XLS vs CSV)](#fonte-de-dados-xls-vs-csv)  
9. [Executando a Aplicação](#executando-a-aplicação)  
10. [Exemplos de Perguntas](#exemplos-de-perguntas)  
11. [Estrutura de Pastas](#estrutura-de-pastas)  
12. [Solução de Problemas](#solução-de-problemas)  
13. [Contribuindo](#contribuindo)  

---

## Visão Geral

1. **Leitura de dados**  
   - Carrega uma planilha XLS ou CSV com cabeçalho e itens de notas fiscais.  
2. **Pergunta do usuário**  
   - Usuário digita uma pergunta no navegador.  
3. **Geração de snippet**  
   - O LangChain envia um prompt ao modelo OpenAI para gerar um trecho de código Python que consulta o DataFrame.  
4. **Execução e formatação**  
   - O snippet é executado (`eval`) e o resultado é formatado em português.  
5. **Resposta**  
   - A resposta final é exibida na interface Streamlit.  

---

## Pré-requisitos

- **Git**  
- **Python 3.8 ou superior**  
- **pip** (gerenciador de pacotes)  
- (Opcional) **virtualenv** ou **venv**  

---

## Clonando o Repositório

No seu terminal (PowerShell, bash, etc.):

```bash
git clone https://github.com/SEU-USUARIO/BrainAI.git
```

---

## Entrando na Pasta do Projeto

```bash
# No Windows PowerShell
cd .\BrainAI\

# No macOS / Linux
cd BrainAI/
```

---

## Criando e Ativando o Ambiente Virtual

### Windows (PowerShell)

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

> Após ativar, seu prompt mudará para algo como `(venv) …`.

---

## Instalando Dependências

1. Atualize o `pip` (opcional, mas recomendado):

   ```bash
   pip install --upgrade pip
   ```

2. Instale todas as bibliotecas listadas em `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

**Dependências principais**:

- `python-dotenv`  
- `streamlit`  
- `pandas`  
- `openai`  
- `langchain`  
- `xlrd` ou `openpyxl` (para XLS)  
- `tabulate`  

---

## Configurando a API Key da OpenAI

1. Crie um arquivo `.env` na raiz do projeto.  
2. Adicione dentro dele:
   ```dotenv
   OPENAI_API_KEY=sk-…
   ```
3. **Importante**: O `.env` já está listado em `.gitignore` para não vazar sua chave.

---

## Fonte de Dados (XLS vs CSV)

O projeto suporta duas formas de entrada de dados:

- **XLS** (arquivo único):  
  - `202401_NFs_Itens.xls`  
- **CSV** (duas tabelas dentro de `202401_NFs/`):  
  - `202401_NFs/202401_NFs_Cabecalho.csv`  
  - `202401_NFs/202401_NFs_Itens.csv`  

Para alternar entre XLS e CSV, edite a variável `CSV_PATH` em **`app.py`**:

```python
# Use XLS (padrão):
CSV_PATH = "202401_NFs_Itens.xls"

# Ou use CSV:
CSV_PATH = "202401_NFs/202401_NFs_Itens.csv"
```

---

## Executando a Aplicação

Com o ambiente virtual ativado e dependências instaladas, basta:

```bash
streamlit run app.py
```

- **Acesse** no navegador: `http://localhost:8501`  
- **Digite** sua pergunta no campo “Digite sua pergunta aqui:”  

---

## Exemplos de Perguntas

- `Qual o valor total de todas as notas?`  
- `Quais as UFs de destino mais frequentes?`  
- `Quem são os três maiores destinatários?`  
- `Quantas notas foram emitidas em 15/01/2024?`  

---

## Estrutura de Pastas

```
BrainAI/
├── .env                     # Variáveis de ambiente (não versionar)
├── .gitignore               # Ignora .env, __pycache__, etc.
├── requirements.txt         # Lista de dependências
├── agente.py                # Lógica interna do agente (LangChain + eval)
├── app.py                   # Interface Streamlit
├── 202401_NFs_Itens.xls     # Planilha Excel de itens
└── 202401_NFs/              # Alternativa em CSV
    ├── 202401_NFs_Cabecalho.csv
    └── 202401_NFs_Itens.csv
```

---

## Solução de Problemas

- **Erro ao ler planilha XLS**  
  - Instale `xlrd`:  
    ```bash
    pip install xlrd
    ```  
  - Verifique se o caminho (`CSV_PATH`) está correto.  
- **API Key não encontrada**  
  - Confirme se `.env` está no mesmo nível de `app.py`.  
  - Confira nome e valor da variável `OPENAI_API_KEY`.  
- **Permissões no terminal**  
  - No PowerShell, se necessário:  
    ```powershell
    Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
    ```

---

## Contribuindo

1. **Fork** deste repositório  
2. Crie uma **branch**:  
   ```bash
   git checkout -b feature/minha-melhoria
   ```
3. Faça seu **commit** & **push**  
4. Abra um **Pull Request**  

