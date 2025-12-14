import numpy as np
import matplotlib.pyplot as plt
from grau_aumento import aumento_grau
from bezier_utils import bezier_curve

# Curva de Bézier quadrática
P = np.array([[0, 0], [1, 2], [4, 0]])
print(f"Curva original - grau {len(P)-1}: {P}")

# Aumentar o grau
Q = aumento_grau(P)
print(f"Curva após aumento de grau - grau {len(Q)-1}: {Q}")

# Plotar as curvas
C1 = bezier_curve(P)
C2 = bezier_curve(Q)

plt.figure(figsize=(10, 6))
plt.plot(C1[:,0], C1[:,1], 'b-', linewidth=2, label="Original (quadrática)")
plt.plot(C2[:,0], C2[:,1], 'r--', linewidth=2, label="Aumento de grau (cúbica)")
plt.scatter(P[:,0], P[:,1], color='blue', s=80, label='Pontos controle originais')
plt.scatter(Q[:,0], Q[:,1], color='red', s=80, label='Novos pontos controle')
plt.legend()
plt.title("Aumento de Grau de Curva de Bézier")
plt.grid(True, alpha=0.3)
plt.axis('equal')
plt.show()

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