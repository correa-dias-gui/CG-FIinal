import numpy as np

def de_casteljau(P, t):
    P = np.array(P, dtype=float)
    n = len(P)
    for r in range(1, n):
        P = (1 - t) * P[:-1] + t * P[1:]
    return P[0]
