import numpy as np

def luminance(img):
    return float(np.mean(img))

def contrast(img):
    return float(np.var(img))

def profondeur(img):
    return int(np.max(img))

import numpy as np

def Ouvrir(img):
    img = np.array(img)
    if len(img.shape) == 3:
        gris = img.mean(axis=0)
        return gris.astype(int)
    elif len(img.shape) == 2:
        return img
    else:
        raise ValueError("Format d'image non supporté")
