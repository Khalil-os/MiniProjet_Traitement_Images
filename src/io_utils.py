import matplotlib.pyplot as plt
import numpy as np
import os

def lectureImage(chemin):
    if not os.path.exists(chemin):
        raise FileNotFoundError(f"ERREUR : Le fichier '{chemin}' n'existe pas.")
    return plt.imread(chemin)

def AfficherImg(img, gray=False):
    img = np.array(img)

    plt.axis("off")

    if gray:
        plt.imshow(img, cmap="gray")
    else:
        if img.ndim == 3 and img.shape[0] == 3:
            img = np.transpose(img, (1, 2, 0))
        plt.imshow(img)

    plt.show()

def saveImage(img, nom="image_sauvegarde.png"):
    img = np.array(img)

    if img.ndim == 3 and img.shape[0] == 3:
        img = np.transpose(img, (1, 2, 0))

    img = img.astype(np.uint8)
    plt.imsave(nom, img)
