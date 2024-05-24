import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

# Configurar a página do Streamlit
st.set_page_config(page_title="Dashboard Biblioteca Pública", layout="wide")
st.title("Dashboard de Indicadores de Atendimento - Biblioteca Pública")

# Carregar dados
file_path = "estatisticaBPP_2023.xlsx"
df = pd.read_excel(file_path, index_col=0)

# Verificação da estrutura dos dados
if df.empty:
    st.error("A planilha está vazia ou o caminho do arquivo está incorreto.")
    st.stop()

# Sidebar para seleção de categoria e mês
st.sidebar.title("Filtros")
categoria = st.sidebar.selectbox("Selecione a Categoria", df.index)
mes = st.sidebar.selectbox("Selecione o Mês", df.columns)

# Filtrar dados de acordo com a seleção
df_filtrado = df.loc[categoria, mes]

# Layout das informações gerais
st.subheader(f"Total Mensal de {categoria} em {mes}")
st.write(f"Quantidade: {df_filtrado}")

# Exibir total anual da categoria selecionada
total_anual = df.loc[categoria].sum()
st.subheader(f"Total Anual de {categoria}")
st.write(f"Quantidade: {total_anual}")

# Gráfico mensal da categoria selecionada
st.subheader(f"Gráfico Mensal de {categoria}")
fig_bar = px.bar(df.loc[categoria], x=df.columns, y=df.loc[categoria].values, title=f'Total Mensal de {categoria}')
st.plotly_chart(fig_bar)

# Gráfico de todos os indicadores no mês selecionado
st.subheader(f"Gráfico de Todos os Indicadores em {mes}")
fig_pie = px.pie(df, names=df.index, values=df[mes], title=f'Totais de Indicadores em {mes}')
st.plotly_chart(fig_pie)

# Exibir totais anuais de todos os indicadores
st.subheader("Totais Anuais de Todos os Indicadores")
totais_anuais = df.sum(axis=1).reset_index()
totais_anuais.columns = ['Indicador', 'Total Anual']
st.write(totais_anuais)

# Exibir os dados filtrados
st.subheader("Dados Filtrados")
st.dataframe(df)

# Configurar o rodapé
st.markdown("---")
st.markdown("Dashboard desenvolvido para visualização dos indicadores de atendimento da Biblioteca Pública.")

