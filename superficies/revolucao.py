import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from bezier.de_casteljau import de_casteljau

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
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x,y,z, s=1)
plt.show()
