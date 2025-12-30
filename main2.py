import numpy as np

from src.io_utils import lectureImage, AfficherImg, saveImage
from src.gris_utils import luminance, contrast, profondeur, Ouvrir
from src.operations_utils import inverser, flipH, poserV, poserH
from src.nb_utils import image_noire, image_blanche, creerImgBlancNoir, negatif
from src.rgb_utils import initImageRGB, symetrie_horizontale, symetrie_verticale, grayscale


def to_np(img):
    return np.array(img)

def info(img):
    a = to_np(img)
    return f"shape={a.shape}, dtype={a.dtype}, min={a.min() if a.size else 'NA'}, max={a.max() if a.size else 'NA'}"

def show_menu():
    print("\n" + "="*55)
    print("MENU")
    print("1) Lire image (lectureImage)")
    print("2) Afficher image actuelle")
    print("3) Save image actuelle")
    print("4) RGB -> Gris (Ouvrir)")
    print("5) Mesures (luminance/contrast/profondeur)")
    print("6) Inverser (255-img)")
    print("7) flipH")
    print("8) poserV")
    print("9) poserH")
    print("10) Create Binary: noire/blanche/damier")
    print("11) Negatif Binary (0<->1)")
    print("12) Create RGB random + symetries + grayscale(min-max)")
    print("0) Quitter")

def main():
    current = None
    mode = None  # 'gray', 'rgb', 'binary'

    while True:
        show_menu()
        if current is None:
            print("[STATUS] no image loaded")
        else:
            print(f"[STATUS] mode={mode} | {info(current)}")

        c = input("Choix: ").strip()

        try:
            if c == "0":
                print("Bye")
                break

            elif c == "1":
                path = input("Chemin: ").strip()
                img = lectureImage(path)
                img = np.array(img)
                current = img
                mode = "rgb" if img.ndim == 3 else "gray"
                print("loaded")

            elif c == "2":
                if current is None:
                    print("load/create image first")
                    continue
                if mode == "rgb":
                    AfficherImg(current, gray=False)
                else:
                    AfficherImg(current, gray=True)

            elif c == "3":
                if current is None:
                    print("no image")
                    continue
                name = input("Nom fichier (ex: out.png): ").strip()
                if name == "":
                    name = "image_sauvegarde.png"
                if mode == "binary":
                    img_save = (to_np(current) * 255).astype(np.uint8)
                    saveImage(img_save, name)
                else:
                    saveImage(current, name)
                print(f"saved: {name}")

            elif c == "4":
                if current is None:
                    print("no image")
                    continue
                current = Ouvrir(current)
                mode = "gray"
                print("converted to gray")

            elif c == "5":
                if current is None:
                    print("no image")
                    continue
                img = current
                if to_np(img).ndim == 3:
                    img = Ouvrir(img)
                print("luminance =", luminance(img))
                print("contrast  =", contrast(img))
                print("profondeur=", profondeur(img))

            elif c == "6":
                if current is None:
                    print("no image")
                    continue
                img = current
                if to_np(img).ndim == 3:
                    img = Ouvrir(img)
                    mode = "gray"
                current = inverser(img)
                mode = "gray"
                print("inverser done")

            elif c == "7":
                if current is None:
                    print("no image")
                    continue
                current = flipH(current)
                print("flipH done")

            elif c == "8":
                if current is None:
                    print("no image")
                    continue
                path2 = input("Chemin 2eme image: ").strip()
                img2 = lectureImage(path2)
                img1 = to_np(current)
                img2 = to_np(img2)
                if img1.ndim == 3: img1 = Ouvrir(img1)
                if img2.ndim == 3: img2 = Ouvrir(img2)
                current = poserV(img1, img2)
                mode = "gray"
                print("poserV done")

            elif c == "9":
                if current is None:
                    print("no image")
                    continue
                path2 = input("Chemin 2eme image: ").strip()
                img2 = lectureImage(path2)
                img1 = to_np(current)
                img2 = to_np(img2)
                if img1.ndim == 3: img1 = Ouvrir(img1)
                if img2.ndim == 3: img2 = Ouvrir(img2)
                current = poserH(img1, img2)
                mode = "gray"
                print("poserH done")

            elif c == "10":
                h = int(input("h: "))
                l = int(input("l: "))
                print("a) noire   (0)")
                print("b) blanche (1)")
                print("c) damier  ((i+j)%2)")
                sub = input("choix a/b/c: ").strip().lower()
                if sub == "a":
                    current = image_noire(h, l)
                elif sub == "b":
                    current = image_blanche(h, l)
                elif sub == "c":
                    current = creerImgBlancNoir(h, l)
                else:
                    print("bad choice")
                    continue
                mode = "binary"
                print("binary image created")

            elif c == "11":
                if current is None or mode != "binary":
                    print("Vous devez d'abord créer une image binaire (option 10).")
                    continue
                current = negatif(current)
                mode = "binary"
                print("negatif binary done")

            elif c == "12":
                n = int(input("n (lignes): "))
                m = int(input("m (colonnes): "))
                rgb = initImageRGB(n, m)  # (3,n,m) كـ list
                current = rgb
                mode = "rgb"
                print("RGB random created (3,n,m)")

                print("a) symetrie horizontale")
                print("b) symetrie verticale")
                print("c) grayscale (min-max)")
                sub = input("choix a/b/c: ").strip().lower()
                if sub == "a":
                    current = symetrie_horizontale(current)
                    print("symetrie horizontale done")
                elif sub == "b":
                    current = symetrie_verticale(current)
                    print("symetrie verticale done")
                elif sub == "c":
                    current = grayscale(current)
                    mode = "gray"
                    print("grayscale done")
                else:
                    print("bad choice")

            else:
                print("choix inconnu")

        except Exception as e:
            print("ERROR:", e)


if __name__ == "__main__":
    main()
