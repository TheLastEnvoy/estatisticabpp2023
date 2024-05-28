import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objs as go

# Dados da planilha
data = {
    "Mês": ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"],
    "Livros recebidos do balcão": [394, 376, 596, 526, 511, 477, 386, 469, 414, 355, 156, 216],
    "Livros recebidos de outras seções": [14, 6, 6, 12, 2, 5, 2, 10, 10, 7, 1, 5],
    "Livros dispersos nas mesas e estantes": [814, 544, 644, 418, 532, 462, 875, 643, 475, 449, 142, 309],
    "Livros recebidos da técnica inéditos em acervo": [88, 82, 146, 94, 120, 72, 49, 57, 142, 89, 40, 49],
    "Livros recebidos da técnica 'já em acervo'": [238, 110, 125, 105, 153, 25, 48, 78, 46, 69, 56, 8],
    "Livros apanhados no depósito": [3, 0, 2, 2, 2, 1, 0, 0, 1, 0, 0, 0],
    "Livros devolvidos ao depósito": [2, 0, 3, 4, 1, 1, 0, 0, 0, 2, 0, 1],
    "Livros devolvidos às estantes": [1548, 1089, 1078, 1083, 1286, 1045, 1360, 1257, 1087, 948, 395, 587],
    "Livros devolvidos às outras seções": [18, 5, 3, 23, 18, 4, 26, 5, 5, 3, 0, 47],
    "Consultas ao terminal (Pergamum)": [113, 82, 147, 89, 140, 103, 75, 84, 100, 60, 39, 44],
    "Consultas ao acervo físico": [86, 49, 137, 101, 155, 158, 121, 117, 143, 144, 53, 106],
    "Chamadas no telefone": [2, 19, 23, 10, 21, 11, 8, 7, 8, 8, 6, 5],
    "Encaminhamento de usuário(a) para outra seção": [14, 14, 18, 16, 17, 15, 6, 12, 27, 18, 6, 18],
    "Livros levados para cópia (xerox)": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Livros selecionados para compor o acervo": [300, 170, 100, 180, 45, 96, 127, 216, 0, 233, 26, 100],
    "Livros não selecionados": [27, 92, 67, 115, 36, 164, 135, 197, 0, 104, 16, 21],
    "Livros baixados": [6, 0, 0, 19, 0, 13, 30, 134, 783, 20, 9, 2],
    "Livros selecionados para depósito": [0, 19, 0, 2, 0, 164, 6, 0, 0, 0, 0, 0],
    "Livros enviados para preservação": [3, 3, 5, 4, 0, 0, 2, 14, 12, 2, 2, 3],
    "Livros enviados para a técnica": [77, 52, 30, 16, 30, 70, 7, 9, 26, 0, 9, 4],
    "Livros restaurados em sala": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Estantes revisadas": [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
    "Estantes organizadas": [39, 14, 0, 6, 0, 0, 3, 0, 0, 0, 0, 0],
    "Livros da técnica conferidos": [311, 202, 288, 200, 252, 97, 77, 113, 156, 129, 41, 59],
    "Livros 'apagados'": [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    "Livros inventariados": [307, 182, 158, 160, 221, 97, 62, 73, 156, 129, 10, 59]
}

df = pd.DataFrame(data)

# Configuração do Streamlit
st.title("BPP - Seção de Ciências Sociais e Jurídicas 2023")

# Quadros de Métricas Chave
st.header("Quantidades totais de 2023")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Consultas ao terminal", value=sum(df["Consultas ao terminal (Pergamum)"]), delta=None, help=None, label_visibility="visible")
    st.metric(label="Consultas ao acervo físico", value=sum(df["Consultas ao acervo físico"]), delta=None, help=None, label_visibility="visible")
with col2:
    st.metric(label="Livros reorganizados", value=sum(df["Livros devolvidos às estantes"]), delta=None, help=None, label_visibility="visible")
    st.metric(label="Livros dispersos", value=sum(df["Livros dispersos nas mesas e estantes"]), delta=None, help=None, label_visibility="visible")
with col3:
    st.metric(label="Livros recebidos do balcão", value=sum(df["Livros recebidos do balcão"]), delta=None, help=None, label_visibility="visible")
    st.metric(label="Livros recebidos das seções", value=sum(df["Livros recebidos de outras seções"]), delta=None, help=None, label_visibility="visible")
with col4:
    st.metric(label="Livros da técnica conferidos", value=sum(df["Livros da técnica conferidos"]), delta=None, help=None, label_visibility="visible")
    st.metric(label="Livros inventariados", value=sum(df["Livros inventariados"]), delta=None, help=None, label_visibility="visible")

# Seleção de Métrica e Tipo de Gráfico
st.header("Gráficos por atividade")
metric = st.selectbox("Selecione a atividade:", options=df.columns[1:], index=0)
chart_type = st.selectbox("Selecione o tipo de gráfico:", ["Linha", "Barra"], index=0)

# Criar gráfico com Plotly
if chart_type == "Linha":
    fig = px.line(df, x="Mês", y=metric, title=f"{metric} - Gráfico de Linha")
elif chart_type == "Barra":
    fig = px.bar(df, x="Mês", y=metric, title=f"{metric} - Gráfico de Barra")

# Exibir gráfico no Streamlit
st.plotly_chart(fig)

# Adicionar tabela com os dados
st.header("Quadro detalhado")
st.dataframe(df)
