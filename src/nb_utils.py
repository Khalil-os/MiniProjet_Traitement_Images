import matplotlib.pyplot as plt

# --- Question 3: Image Noire ---
def image_noire(h, l):
    # F C, hada howa l-equivalent dyal double malloc (lignes + colonnes) + bzero
    matrice = [] 
    for i in range(h):           # Pour chaque ligne
        ligne = []
        for j in range(l):       # Pour chaque colonne
            ligne.append(0)      # 0 = Noir
        matrice.append(ligne)    # Ajouti l-ligne l l-matrice kbira
    return matrice

# --- Question 4: Image Blanche ---
def image_blanche(h, l):
    # Nafss l-plan, ghir hna kan3mro b 1
    matrice = []
    for i in range(h):
        ligne = []
        for j in range(l):
            ligne.append(1)      # 1 = Blanc
        matrice.append(ligne)
    return matrice

# --- Question 5: Image Damier (Blanc et Noir) ---
def creerImgBlancNoir(h, l):
    # Hna fin kayn l-logic dyal l-damier
    matrice = []
    for i in range(h):
        ligne = []
        for j in range(l):
            # L-formule mn l-pdf: (i + j) % 2
            valeur = (i + j) % 2 
            ligne.append(valeur)
        matrice.append(ligne)
    return matrice

# --- Question 6: Négatif ---
def negatif(img):
    h = len(img)        # Nombre de lignes
    l = len(img[0])     # Nombre de colonnes
    
    # Khassna n-creer image jdida bach man-modifiwch l-originale (Copie)
    img_neg = []
    
    for i in range(h):
        ligne = []
        for j in range(l):
            pixel_original = img[i][j]
            # Logic dyal l-inversion:
            # Ila kan 0 -> ywlli 1
            # Ila kan 1 -> ywlli 0
            # A7san tariqa mathématique: 1 - pixel
            pixel_inverse = 1 - pixel_original
            ligne.append(pixel_inverse)
        img_neg.append(ligne)
        
    return img_neg
