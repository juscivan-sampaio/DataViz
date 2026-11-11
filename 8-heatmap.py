import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

empresas = ['Empresa A', 'Empresa B', 'Empresa C', 'Empresa D']
trimestres = ['T1', 'T2', 'T3', 'T4']

dados = np.random.rand(4, 4) * 100

df = pd.DataFrame(
    dados,
    columns=trimestres,
    index=empresas
)

plt.figure(figsize=(8, 6))
sns.heatmap(df, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Preço de Acoes por Trimestre')
plt.xlabel('Trimestre')
plt.ylabel('Empresa')
plt.show()