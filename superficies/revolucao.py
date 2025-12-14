import numpy as np
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from bezier.de_casteljau import de_casteljau
from visualizacao import plot_surface_3d

def superficie_revolucao(P, samples=50):
    u = np.linspace(0,1,samples)
    theta = np.linspace(0,2*np.pi,samples)

    Sx, Sy, Sz = [], [], []

    for t in u:
        p = de_casteljau(P, t)
        for th in theta:
            Sx.append(p[0]*np.cos(th))
            Sy.append(p[0]*np.sin(th))
            Sz.append(p[1])

    return np.array(Sx), np.array(Sy), np.array(Sz)

P = [[1,0], [2,2], [1,4]]

x,y,z = superficie_revolucao(P)

# Combinar coordenadas em um array para visualização
points = np.column_stack((x, y, z))

print(f"Superfície de revolução gerada com {len(points)} pontos")

if 'matplotlib' in sys.argv:
    print("Usando matplotlib para visualização")
else:
    print("Usando OpenGL para visualização (use 'matplotlib' como argumento para matplotlib)")

plot_surface_3d(points, "Superfície de Revolução")
