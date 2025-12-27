import numpy as np

def inverser(img):
    return 255 - img

def flipH(img):
    return np.flip(img, axis=1)

def poserV(img1, img2):
	if img1.shape[1] != img2.shape[1]:
		raise ValueError("Les deux images doivent avoir la même largeur.")
	return np.vstack((img1, img2))

def poserH(img1, img2):
	if img1.shape[0] != img2.shape[0]:
		raise ValueError("Les deux images doivent avoir la même hauteur.")
	return np.hstack((img1, img2))