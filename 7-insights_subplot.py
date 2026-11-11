import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data/Pedidos.csv')

fig, ax= plt.subplots(2, 2, figsize=(15, 15))

df.groupby('Regiao')['Unidades'].sum().plot(kind='bar', color='skyblue', ax=ax[0, 0])
ax[0, 0].set_title('Quantidade de Unidades vendidas por região')
ax[0, 0].set_xlabel('Região')
ax[0, 0].set_ylabel('Total de Unidades Vendidas')
ax[0, 0].tick_params(axis='x', rotation=45)

df['Item'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, ax=ax[0, 1])
ax[0, 1].set_title('Distribuição das vendas por item')
ax[00, 1].axis('equal')


ax[1, 0].scatter(
    df['PrecoUnidade'],
    df['Unidades'],
    color='orange'
)
ax[1, 0].set_title('Relação entre preco unitario e quantitativo de unidades')
ax[1, 0].set_xlabel('Preço Unitario')
ax[1, 0].set_ylabel('Quantidade de Unidades')
ax[1, 0].grid(True)

df.groupby('DataPedido')['Unidades'].sum().plot(kind='line', marker='o', color='green', ax=ax[1, 1])
ax[1, 1].set_title('Quantidade de unidades vendidas ao longo do tempo')
ax[1, 1].set_xlabel('Data do pedido')
ax[1, 1].set_ylabel('Total de unidades vendidas')
ax[1, 1].grid(True)


plt.show()