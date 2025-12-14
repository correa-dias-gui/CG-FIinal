import numpy as np
from de_casteljau import de_casteljau

def bezier_curve(P, samples=100):
    return np.array([de_casteljau(P, t) for t in np.linspace(0, 1, samples)])
