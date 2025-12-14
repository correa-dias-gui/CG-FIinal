import numpy as np
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from bezier.de_casteljau import de_casteljau

def varredura(curva, altura=5, samples=50):
    u = np.linspace(0,1,samples)
    v = np.linspace(0,altura,samples)

    X,Y,Z = [],[],[]
    for z in v:
        for t in u:
            p = de_casteljau(curva, t)
            X.append(p[0])
            Y.append(p[1])
            Z.append(z)
    return X,Y,Z
