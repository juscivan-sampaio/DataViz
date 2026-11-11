import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

categorias = ['Eletronicos', 'Roupas', 'Alimentos', 'Livros']
vendas = {
    'Categoria': np.random.choice(categorias, 100),
    'Vendas': np.random.normal(loc=50, scale=20, size=100)
}

df = pd.DataFrame(vendas)

plt.figure(figsize=(8, 6))
sns.violinplot(
    x='Categoria',
    y='Vendas',
    data=df,
    palette='muted'
)
plt.title('Distribuição de vendas por categoria')
plt.xlabel('Categoria')
plt.ylabel('Vendas')
plt.show()