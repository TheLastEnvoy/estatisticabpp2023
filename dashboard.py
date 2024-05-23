import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados
file_path = "estatisticaBPP_2023.xlsx"
df = pd.read_excel(file_path)

# Sidebar para seleção de categoria e mês
st.sidebar.title("Filtros")
categoria = st.sidebar.selectbox("Selecione a Categoria", df.columns[1:])
mes = st.sidebar.selectbox("Selecione o Mês", df['Mês'].unique())

# Filtrar dados de acordo com a seleção
df_filtrado = df[df['Mês'] == mes]

# Exibir total mensal da categoria selecionada
total_mensal = df_filtrado[categoria].sum()
st.header(f"Total Mensal de {categoria} em {mes}")
st.subheader(total_mensal)

# Exibir total anual da categoria selecionada
total_anual = df[categoria].sum()
st.header(f"Total Anual de {categoria}")
st.subheader(total_anual)

# Gráfico mensal da categoria selecionada
fig, ax = plt.subplots()
df.groupby('Mês')[categoria].sum().plot(kind='bar', ax=ax)
ax.set_title(f'Total Mensal de {categoria}')
ax.set_xlabel('Mês')
ax.set_ylabel('Quantidade')
st.pyplot(fig)

# Gráfico de todos os indicadores no mês selecionado
fig, ax = plt.subplots(figsize=(10, 6))
df_filtrado.set_index('Mês').T.plot(kind='bar', ax=ax)
ax.set_title(f'Totais de Indicadores em {mes}')
ax.set_xlabel('Indicadores')
ax.set_ylabel('Quantidade')
st.pyplot(fig)

# Exibir totais anuais de todos os indicadores
st.header("Totais Anuais de Todos os Indicadores")
totais_anuais = df.groupby('Mês').sum().sum(axis=0)
st.dataframe(totais_anuais)

# Rodar o Streamlit app
if __name__ == "__main__":
    st.set_page_config(page_title="Dashboard Biblioteca Pública", layout="wide")
    st.title("Dashboard de Indicadores de Atendimento - Biblioteca Pública")
    st.markdown("### Selecione a categoria e o mês para visualizar os dados.")

    # Exibir os gráficos e dados
    st.pyplot(fig)
    st.dataframe(df_filtrado)

