import numpy as np
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from bezier.de_casteljau import de_casteljau

def asa(curva, comprimento=10, samples=50):
    pontos = []
    for v in np.linspace(0,1,samples):
        escala = 1 - 0.7*v
        for t in np.linspace(0,1,samples):
            p = de_casteljau(curva, t)
            pontos.append([escala*p[0], escala*p[1], comprimento*v])
    return np.array(pontos)
