from src.io_utils import lectureImage, AfficherImg, saveImage
from src.nb_utils import image_noire, image_blanche, creerImgBlancNoir, negatif
from src.gris_utils import luminance, contrast, profondeur, Ouvrir
from src.operations_utils import inverser, flipH, poserV, poserH
from src.rgb_utils import initImageRGB, symetrie_verticale, symetrie_horizontale, grayscale

import numpy as np


def test_io():
    print("=== TEST IO ===")
    img = lectureImage("images/input/test.jpg")
    AfficherImg(img)
    saveImage(img, "copie_test.png")


def test_noir_blanc():
    print("=== TEST NOIR & BLANC ===")
    img_noire = image_noire(5, 5)
    img_blanche = image_blanche(5, 5)
    img_chess = creerImgBlancNoir(8, 8)
    img_neg = negatif(img_chess)

    AfficherImg(img_noire, gray=True)
    AfficherImg(img_blanche, gray=True)
    AfficherImg(img_chess, gray=True)
    AfficherImg(img_neg, gray=True)


def test_gris():
    print("=== TEST NIVEAUX DE GRIS ===")
    img = np.array([
        [10, 50, 200],
        [30, 80, 255],
        [0, 100, 150]
    ])

    print("Luminance :", luminance(img))
    print("Contrast  :", contrast(img))
    print("Profondeur:", profondeur(img))

    img_inv = inverser(img)
    AfficherImg(img_inv, gray=True)


def test_ouvrir():
    print("=== TEST OUVRIR ===")

    img_rgb = initImageRGB(4, 6)
    AfficherImg(img_rgb)

    img_gris = Ouvrir(img_rgb)
    AfficherImg(img_gris, gray=True)

    img_gris2 = np.array([
        [20, 60, 120],
        [30, 90, 200]
    ])
    img_gris2_out = Ouvrir(img_gris2)
    AfficherImg(img_gris2_out, gray=True)


def test_operations():
    print("=== TEST OPERATIONS (VISUEL) ===")
    img1 = np.array([
        [  0,  50, 100, 150, 200],
        [  0,  50, 100, 150, 200],
        [  0,  50, 100, 150, 200],
        [  0,  50, 100, 150, 200],
        [  0,  50, 100, 150, 200]
    ])
    img2 = np.array([
        [  0,   0,   0,   0,   0],
        [ 50,  50,  50,  50,  50],
        [100, 100, 100, 100, 100],
        [150, 150, 150, 150, 150],
        [200, 200, 200, 200, 200]
    ])
    AfficherImg(img1, gray=True)
    img_flip = flipH(img1)
    AfficherImg(img_flip, gray=True)
    img_v = poserV(img1, img2)
    AfficherImg(img_v, gray=True)
    img_h = poserH(img1, img2)
    AfficherImg(img_h, gray=True)


def test_rgb():
    print("=== TEST RGB ===")
    img = initImageRGB(4, 6)
    AfficherImg(img)

    img_sym_h = symetrie_horizontale(img)
    AfficherImg(img_sym_h)

    img_sym_v = symetrie_verticale(img)
    AfficherImg(img_sym_v)

    img_gray = grayscale(img)
    AfficherImg(img_gray, gray=True)


def test_negatif_image():
	img = lectureImage("child.jpg")
	img_gris = Ouvrir(img)
	img_B = inverser(img_gris)
	AfficherImg(img_B, gray=True)

if __name__ == "__main__":
    test_negatif_image()
    print("\n>>> Tous les tests sont terminés avec succès !")
