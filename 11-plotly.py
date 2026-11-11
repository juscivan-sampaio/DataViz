import plotly.graph_objs as go
import plotly.express as px
import pandas as pd

data = {
    'Date': pd.date_range(start='2026-01-01', periods=100),
    'StockA': [100 + i for i in range(100)],
    'StockB': [120 - i for i in range(100)],
    'StockC': [90 + (i *0.5) for i in range(100)],
}

df = pd.DataFrame(data)

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=df['Date'],
    y=df['StockA'],
    mode='lines',
    name='Sotck A'
))
fig.add_trace(go.Scatter(
    x=df['Date'],
    y=df['StockB'],
    mode='lines',
    name='Sotck B'
))
fig.add_trace(go.Scatter(
    x=df['Date'],
    y=df['StockC'],
    mode='lines',
    name='Sotck C'
))

fig.update_layout(
    title='Variação de preço ao longo do tempo',
    xaxis_title='Data',
    yaxis_title='Preço',
    hovermode='x'
)

fig.show()