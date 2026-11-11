import matplotlib.pyplot as plt 
import numpy as np

pontuacoes = np.random.randint(50, 100, 100)


plt.figure(figsize=(8, 5))
plt.hist(
    pontuacoes,
    bins=10,
    color='skyblue',
    edgecolor='black'
)

plt.xlabel('Pontuaçao')
plt.ylabel('Frequencia')
plt.title('Distribuição  das Pontuaçoes do Teste')

plt.show()