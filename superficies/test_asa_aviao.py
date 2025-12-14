import numpy as np
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from asa_aviao import asa
from bezier.de_casteljau import de_casteljau
from visualizacao import plot_surface_3d

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

print(f"Superfície da asa gerada com {len(pontos)} pontos")
print(f"Redução de escala de 100% na raiz para 30% na ponta")

if 'matplotlib' in sys.argv:
    print("Usando matplotlib para visualização")
else:
    print("Usando OpenGL para visualização (use 'matplotlib' como argumento para matplotlib)")

# Visualizar
plot_surface_3d(pontos, "Superfície de Varredura - Asa de Avião")

print(f"Superfície da asa gerada com {len(pontos)} pontos")
print(f"Redução de escala de 100% na raiz para 30% na ponta")