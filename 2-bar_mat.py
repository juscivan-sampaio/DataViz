import matplotlib.pyplot as plt

#Dados
vendedores = ['João', 'Maria', 'Pedro', 'Ana']
qtd_vendas = [45, 60, 30, 55] 

#Criando Grafico
plt.figure(figsize=(8,5))
plt.bar(
    vendedores,
    qtd_vendas,
    color='green'
)

plt.xlabel('Vendedores')
plt.ylabel('Quantidade')
plt.title('Quantidade de produtos vendido por vendedor')

#exibir grafico
plt.show()