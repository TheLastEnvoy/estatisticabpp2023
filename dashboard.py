import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

# Dados da planilha
data = {
    "Mês": ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"],
    "Recebidos do balcão": [394, 376, 596, 526, 511, 477, 386, 469, 414, 355, 156, 216],
    "Recebidos de outras seções": [14, 6, 6, 12, 2, 5, 2, 10, 10, 7, 1, 5],
    "Dispersos nas mesas e estantes": [814, 544, 644, 418, 532, 462, 875, 643, 475, 449, 142, 309],
    "Recebidos da técnica inéditos em acervo": [88, 82, 146, 94, 120, 72, 49, 57, 142, 89, 40, 49],
    "Recebidos da técnica 'já em acervo'": [238, 110, 125, 105, 153, 25, 48, 78, 46, 69, 56, 8],
    "Apanhados no depósito": [3, 0, 2, 2, 2, 1, 0, 0, 1, 0, 0, 0],
    "Devolvidos ao depósito": [2, 0, 3, 4, 1, 1, 0, 0, 0, 2, 0, 1],
    "Devolvidos às estantes": [1548, 1089, 1078, 1083, 1286, 1045, 1360, 1257, 1087, 948, 395, 587],
    "Devolvidos às outras seções": [18, 5, 3, 23, 18, 4, 26, 5, 5, 3, 0, 47],
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

# Inicializando a aplicação Dash
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard da Biblioteca"),
    dcc.Dropdown(
        id="metric-selector",
        options=[{"label": col, "value": col} for col in df.columns if col != "Mês"],
        value="Recebidos do balcão",
        clearable=False
    ),
    dcc.Graph(id="line-chart"),
])

@app.callback(
    Output("line-chart", "figure"),
    [Input("metric-selector", "value")]
)
def update_chart(selected_metric):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["Mês"], y=df[selected_metric], mode="lines+markers"))
    fig.update_layout(
        title=selected_metric,
        xaxis_title="Mês",
        yaxis_title="Quantidade"
    )
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
