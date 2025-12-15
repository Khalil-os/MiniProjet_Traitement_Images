from src.io_utils import lectureImage, AfficherImg, saveImage
from src.nb_utils import image_noire, image_blanche, creerImgBlancNoir, negatif
from src.gris_utils import luminance, contrast, profondeur, inverser
from src.operations_utils import flipH, poserV, poserH
from src.rgb_utils import initImageRGB, symetrie, grayscale

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


def test_operations():
    print("=== TEST OPERATIONS ===")
    img1 = np.ones((5, 5)) * 80
    img2 = np.ones((5, 5)) * 200

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

    img_sym = symetrie(img)
    AfficherImg(img_sym)

    img_gray = grayscale(img)
    AfficherImg(img_gray, gray=True)


if __name__ == "__main__":
    test_io()
    test_noir_blanc()
    test_gris()
    test_operations()
    test_rgb()

    print("\n>>> Tous les tests sont terminés avec succès !")
