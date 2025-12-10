import numpy as np

def luminance(img):
    return float(np.mean(img))

def contrast(img):
    return float(np.var(img))

def profondeur(img):
    return int(np.max(img))

def inverser(img):
    return 255 - img