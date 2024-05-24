import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurar a página do Streamlit
st.set_page_config(page_title="Dashboard Biblioteca Pública", layout="wide")
st.title("Dashboard de Indicadores de Atendimento - Biblioteca Pública")
st.markdown("### Selecione a categoria e o mês para visualizar os dados.")

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

# Exibir total mensal da categoria selecionada
st.header(f"Total Mensal de {categoria} em {mes}")
st.subheader(df_filtrado)

# Exibir total anual da categoria selecionada
total_anual = df.loc[categoria].sum()
st.header(f"Total Anual de {categoria}")
st.subheader(total_anual)

# Gráfico mensal da categoria selecionada
st.header(f"Gráfico Mensal de {categoria}")
fig, ax = plt.subplots()
sns.barplot(x=df.columns, y=df.loc[categoria], palette="viridis", ax=ax)
ax.set_title(f'Total Mensal de {categoria}')
ax.set_xlabel('Mês')
ax.set_ylabel('Quantidade')
st.pyplot(fig)

# Gráfico de todos os indicadores no mês selecionado
st.header(f"Gráfico de Todos os Indicadores em {mes}")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=df.index, y=df[mes], palette="viridis", ax=ax)
ax.set_title(f'Totais de Indicadores em {mes}')
ax.set_xlabel('Indicadores')
ax.set_ylabel('Quantidade')
plt.xticks(rotation=90)
st.pyplot(fig)

# Exibir totais anuais de todos os indicadores
st.header("Totais Anuais de Todos os Indicadores")
totais_anuais = df.sum(axis=1)
st.dataframe(totais_anuais)

# Exibir os gráficos e dados
st.header("Dados Filtrados")
st.dataframe(df)
