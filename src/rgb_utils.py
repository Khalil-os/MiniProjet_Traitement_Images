
from random import randrange

def initImageRGB(n, m):
    imageRGB = []
    for c in range(3):                 # 3 couches : R, G, B
        couche = []
        for i in range(n):            # lignes
            ligne = []
            for j in range(m):        # colonnes
                ligne.append(randrange(256))   # valeur 0-255
            couche.append(ligne)
        imageRGB.append(couche)
    return imageRGB

def symetrie_horizontale(img):
    return [ [ligne[::-1] for ligne in couche] for couche in img ]

def symetrie_verticale(img):
    return [ couche[::-1] for couche in img ]

def grayscale(imageRGB):
    n = len(imageRGB[0])       # nombre de lignes
    m = len(imageRGB[0][0])    # nombre de colonnes

    img_gray = []

    for i in range(n):
        ligne = []
        for j in range(m):

            r = imageRGB[0][i][j]
            g = imageRGB[1][i][j]
            b = imageRGB[2][i][j]

            maxi = max(r, g, b)
            mini = min(r, g, b)
            gray = (maxi + mini) // 2

            ligne.append(gray)

        img_gray.append(ligne)

    return img_gray

