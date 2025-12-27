from random import randrange

# Création d'une image RGB (3 × n × m)
def initImageRGB(n, m):
    imageRGB = []
    for c in range(3):
        couche = []
        for i in range(n):
            ligne = []
            for j in range(m):
                ligne.append(randrange(256))  # pixel entre 0 et 255
            couche.append(ligne)
        imageRGB.append(couche)
    return imageRGB


# Symétrie horizontale (gauche ↔ droite)
def symetrie_horizontale(img):
    return [[ligne[::-1] for ligne in couche] for couche in img]


# Symétrie verticale (haut ↔ bas)
def symetrie_verticale(img):
    return [couche[::-1] for couche in img]


# Conversion RGB → niveaux de gris (méthode min–max)
def grayscale(imageRGB):
    n = len(imageRGB[0])
    m = len(imageRGB[0][0])
    img_gray = []

    for i in range(n):
        ligne = []
        for j in range(m):
            r = imageRGB[0][i][j]
            g = imageRGB[1][i][j]
            b = imageRGB[2][i][j]
            gray = (max(r, g, b) + min(r, g, b)) // 2
            ligne.append(gray)
        img_gray.append(ligne)

    return img_gray
