import numpy as np
import sys
from grau_reducao import reduzir_cubica_para_quadratica, erro_maximo
from bezier_utils import bezier_curve
from visualizacao import plot_curves_2d

P = np.array([[0,0], [1,2], [3,2], [4,0]])

Q = reduzir_cubica_para_quadratica(P)
erro = erro_maximo(P, Q)

C1 = bezier_curve(P)
C2 = bezier_curve(Q)

# Preparar dados para visualização
curves_data = [
    {
        'points': C1,
        'label': 'Cúbica',
        'color': (0, 0, 1),  # azul
        'line_style': 'solid'
    },
    {
        'points': C2,
        'label': 'Quadrática',
        'color': (1, 0, 0),  # vermelho
        'line_style': 'dashed'
    },
    {
        'points': P,
        'label': 'Pontos controle original',
        'color': (0, 0, 1),  # azul
        'point_style': 'scatter'
    },
    {
        'points': Q,
        'label': 'Pontos controle reduzido',
        'color': (1, 0, 0),  # vermelho
        'point_style': 'scatter'
    }
]

print(f"Erro máximo = {erro:.4f}")
if 'matplotlib' in sys.argv:
    print("Usando matplotlib para visualização")
else:
    print("Usando OpenGL para visualização (use 'matplotlib' como argumento para matplotlib)")

plot_curves_2d(curves_data, f"Redução de Grau - Erro máximo = {erro:.4f}")
