import numpy as np
import matplotlib.pyplot as plt
from grau_reducao import reduzir_cubica_para_quadratica, erro_maximo
from bezier_utils import bezier_curve

P = np.array([[0,0], [1,2], [3,2], [4,0]])

Q = reduzir_cubica_para_quadratica(P)
erro = erro_maximo(P, Q)

C1 = bezier_curve(P)
C2 = bezier_curve(Q)

plt.plot(C1[:,0], C1[:,1], label="Cúbica")
plt.plot(C2[:,0], C2[:,1], '--', label="Quadrática")
plt.scatter(P[:,0], P[:,1])
plt.scatter(Q[:,0], Q[:,1])
plt.legend()
plt.title(f"Erro máximo = {erro:.4f}")
plt.show()
