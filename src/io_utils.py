import matplotlib.pyplot as plt
import numpy as np
import os

def lectureImage(chemin):
    if not os.path.exists(chemin):
        raise FileNotFoundError(f"ERREUR : Le fichier '{chemin}' n'existe pas.")   
    img = plt.imread(chemin)
    return img

def AfficherImg(img, gray=False):
    plt.axis("off")
    if gray:
        plt.imshow(img, cmap="gray")
    else:
        plt.imshow(img)
    plt.show()

def saveImage(img, nom="image_sauvegarde.png"):
    plt.imsave(nom, img)