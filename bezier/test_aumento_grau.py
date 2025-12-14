import numpy as np
import sys
from grau_aumento import aumento_grau
from bezier_utils import bezier_curve
from visualizacao import plot_curves_2d

# Curva de Bézier quadrática
P = np.array([[0, 0], [1, 2], [4, 0]])
print(f"Curva original - grau {len(P)-1}: {P}")

# Aumentar o grau
Q = aumento_grau(P)
print(f"Curva após aumento de grau - grau {len(Q)-1}: {Q}")

# Plotar as curvas
C1 = bezier_curve(P)
C2 = bezier_curve(Q)

# Preparar dados para visualização
curves_data = [
    {
        'points': C1,
        'label': 'Original (quadrática)',
        'color': (0, 0, 1),  # azul
        'line_style': 'solid'
    },
    {
        'points': C2,
        'label': 'Aumento de grau (cúbica)',
        'color': (1, 0, 0),  # vermelho
        'line_style': 'dashed'
    },
    {
        'points': P,
        'label': 'Pontos controle originais',
        'color': (0, 0, 1),  # azul
        'point_style': 'scatter'
    },
    {
        'points': Q,
        'label': 'Novos pontos controle',
        'color': (1, 0, 0),  # vermelho
        'point_style': 'scatter'
    }
]

if 'matplotlib' in sys.argv:
    print("Usando matplotlib para visualização")
else:
    print("Usando OpenGL para visualização (use 'matplotlib' como argumento para matplotlib)")

plot_curves_2d(curves_data, "Aumento de Grau de Curva de Bézier")

# Verificar se as curvas são geometricamente equivalentes
# comparando pontos ao longo da curva
t_values = np.linspace(0, 1, 50)
from de_casteljau import de_casteljau

max_diff = 0
for t in t_values:
    p1 = de_casteljau(P, t)
    p2 = de_casteljau(Q, t)
    diff = np.linalg.norm(p1 - p2)
    max_diff = max(max_diff, diff)

print(f"\nDiferença máxima entre as curvas: {max_diff:.10f}")
print("As curvas são geometricamente equivalentes!" if max_diff < 1e-10 else "Há diferença entre as curvas!")