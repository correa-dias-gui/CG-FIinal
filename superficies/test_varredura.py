import numpy as np
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from varredura import varredura
from bezier.de_casteljau import de_casteljau
from visualizacao import plot_surface_3d

# Definir uma curva de Bézier fechada no plano xy
curva = np.array([
    [0, 0],
    [2, 0],
    [2, 2], 
    [0, 2],
    [0, 0]
])

# Gerar superfície de varredura
X, Y, Z = varredura(curva, altura=5, samples=30)

# Combinar coordenadas em um array para visualização
points = np.column_stack((X, Y, Z))

print(f"Superfície de varredura gerada com {len(points)} pontos")
print("Perfil movido ao longo do eixo Z")

if 'matplotlib' in sys.argv:
    print("Usando matplotlib para visualização")
else:
    print("Usando OpenGL para visualização (use 'matplotlib' como argumento para matplotlib)")

plot_surface_3d(points, "Superfície de Varredura")