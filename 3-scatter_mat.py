import matplotlib.pyplot  as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

x = np.random.rand(50)
y = np.random.rand(50)
z = np.random.rand(50)

plt.figure(figsize=(8,6))
plt.scatter(x, y)
plt.title('Grafico de Dispesão com Dados Aleatorio')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.grid(True)
plt.show()

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y, z)

ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_zlabel('Eixo Z')
ax.set_title('Grafico de Dispesão em 3D')

plt.show()