import matplotlib.pyplot as plt

#Dados
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun']
vendas = [150, 200, 180, 300, 250, 400]

# Criando grafico
plt.figure(figsize=(8, 5))
plt.plot(
    meses,
    vendas,
    marker='o',
    linestyle='-',
    color='blue',
    label='Vendas'
)

#Exibindo Grafico
plt.xlabel('Mes')
plt.ylabel('Vendas')
plt.title('Vendas ao Longo dos Meses')
plt.legend()
plt.grid()

plt.show()