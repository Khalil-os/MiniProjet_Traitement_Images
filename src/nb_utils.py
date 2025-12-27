import matplotlib.pyplot as plt

# --- Question 3: Image Noire ---
def image_noire(h, l):
    matrice = [] 
    for i in range(h):        
        ligne = []
        for j in range(l):      
            ligne.append(0)      
        matrice.append(ligne)  
    return matrice

# --- Question 4: Image Blanche ---
def image_blanche(h, l):

    matrice = []
    for i in range(h):
        ligne = []
        for j in range(l):
            ligne.append(1)      
        matrice.append(ligne)
    return matrice

# --- Question 5: Image Damier (Blanc et Noir) ---
def creerImgBlancNoir(h, l):

    matrice = []
    for i in range(h):
        ligne = []
        for j in range(l):
            valeur = (i + j) % 2 
            ligne.append(valeur)
        matrice.append(ligne)
    return matrice

# --- Question 6: Négatif ---
def negatif(img):
    h = len(img)  
    l = len(img[0])     
    
    img_neg = []
    
    for i in range(h):
        ligne = []
        for j in range(l):
            pixel_original = img[i][j]
            pixel_inverse = 1 - pixel_original
            ligne.append(pixel_inverse)
        img_neg.append(ligne)
        
    return img_neg
