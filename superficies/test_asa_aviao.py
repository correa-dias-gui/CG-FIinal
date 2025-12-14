import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from asa_aviao import asa
from bezier.de_casteljau import de_casteljau

# Definir um perfil de asa (curva de Bézier fechada)
perfil = np.array([
    [0, 0],
    [2, 1],
    [4, 0.5],
    [6, 0],
    [4, -0.3],
    [2, -0.2],
    [0, 0]
])

# Gerar a superfície da asa
pontos = asa(perfil, comprimento=10, samples=30)

# Visualizar
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plotar os pontos
ax.scatter(pontos[:,0], pontos[:,1], pontos[:,2], c=pontos[:,2], cmap='viridis', s=5)

ax.set_xlabel('X')
ax.set_ylabel('Y') 
ax.set_zlabel('Z')
ax.set_title('Superfície de Varredura - Asa de Avião')

plt.show()

print(f"Superfície da asa gerada com {len(pontos)} pontos")
print(f"Redução de escala de 100% na raiz para 30% na ponta")