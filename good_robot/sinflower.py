# AUTOGENERATED! DO NOT EDIT! File to edit: 11_sinflower.ipynb (unless otherwise specified).

__all__ = ['cart2pol', 'pol2cart', 'generalized_sinflower_transform']

# Cell
import pandas as pd, numpy as np, matplotlib.pyplot as plt
from datetime import datetime as dt
import seaborn as sns
from matplotlib.collections import LineCollection
from pathlib import Path
from scipy import spatial
from tqdm import tqdm


from .gram import layer_to_lines, lines_to_layer, Turtle
from good_robot import write

# Cell
def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi)

# Cell
def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

# Cell
def generalized_sinflower_transform(r, Θ, A=1, B=-1, C=-1, D=1, E=1, F=1, G=-1, H=-1, I=1, J=1):
        r_out = A + ((B * r) + (C * np.sin((D * Θ) ** 2))) * E
        Θ_out = F + ((G * Θ) + (H * np.cos((I * r) ** 2))) * J
        return r_out, Θ_out