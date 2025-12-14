import numpy as np

def aumento_grau(P):
    n = len(P) - 1
    Q = [P[0]]
    for i in range(1, n+1):
        alpha = i / (n+1)
        Q.append((1-alpha)*P[i] + alpha*P[i-1])
    Q.append(P[-1])
    return np.array(Q)
