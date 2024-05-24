import streamlit as st
import pandas as pd
import plotly.express as px

# Configurar a página do Streamlit
st.set_page_config(page_title="Dashboard Biblioteca Pública", layout="wide")
st.title("Dashboard de Indicadores de Atendimento - Biblioteca Pública")

# Carregar dados
file_path = "estatisticaBPP_2023.xlsx"
df = pd.read_excel(file_path, index_col=0)

# Remover linhas em branco
df.dropna(how='all', inplace=True)

# Verificação da estrutura dos dados
if df.empty:
    st.error("A planilha está vazia ou o caminho do arquivo está incorreto.")
    st.stop()

# Sidebar para seleção de mês
st.sidebar.title("Filtros")
mes = st.sidebar.selectbox("Selecione o Mês", df.columns)

# Filtrar dados de acordo com a seleção do mês
df_mes = df[[mes]].copy()

# Exibir informações do mês selecionado
st.subheader(f"Informações de {mes}")

# Gráfico de todos os indicadores no mês selecionado
fig_bar_mes = px.bar(df_mes, x=df_mes.index, y=df_mes[mes], title=f'Totais de Indicadores em {mes}', labels={'x': 'Indicador', 'y': 'Quantidade'})
st.plotly_chart(fig_bar_mes)

# Exibir dados filtrados do mês
st.dataframe(df_mes)

# Resumo Anual
st.subheader("Resumo Anual")

# Totais anuais de todos os indicadores
totais_anuais = df.sum(axis=1).reset_index()
totais_anuais.columns = ['Indicador', 'Total Anual']
st.write(totais_anuais)

# Gráfico anual comparativo de todos os indicadores
fig_bar_anual = px.bar(df.T, x=df.columns, y=df.sum(axis=0), title='Comparativo Mensal de Todos os Indicadores', labels={'x': 'Mês', 'y': 'Total'})
st.plotly_chart(fig_bar_anual)

# Gráfico de calor (heatmap) para identificar os meses mais e menos trabalhosos
fig_heatmap = px.imshow(df, labels=dict(x="Mês", y="Indicador", color="Quantidade"), title="Mapa de Calor dos Indicadores ao Longo do Ano")
st.plotly_chart(fig_heatmap)

# Configurar o rodapé
st.markdown("---")
st.markdown("Dashboard desenvolvido para visualização dos indicadores de atendimento da Biblioteca Pública.")
