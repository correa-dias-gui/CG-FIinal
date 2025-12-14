import numpy as np
from bezier_utils import bezier_curve

def reduzir_cubica_para_quadratica(P):
    Q0 = P[0]
    Q2 = P[3]
    Q1 = (3/4)*P[1] + (1/4)*P[2]
    return np.array([Q0, Q1, Q2])

def erro_maximo(P, Q, samples=100):
    Bn = bezier_curve(P, samples)
    Bm = bezier_curve(Q, samples)
    return np.max(np.linalg.norm(Bn - Bm, axis=1))
