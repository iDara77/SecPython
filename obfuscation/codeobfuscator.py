from PIL import Image
import os,math

## Ouvrir le fichier image et extraire la taille pour calculer la taille maximale du code
DIR = os.path.dirname(os.path.realpath(__file__))
IMAGE_ORIG=f"{DIR}/image_orig.jpg"

def loadImage(path):
    with Image.open(path) as img:
        img.load()
    return img

img = loadImage(IMAGE_ORIG)
print(f"Image size: {img.size}")
max_code_size = math.floor(img.size[0]*img.size[1]/8)
print(f"Maximum code length: {max_code_size}")
################

