from PIL import Image
import os,math
import zlib

DIR = os.path.dirname(os.path.realpath(__file__))
IMAGE_ORIG=f"{DIR}/image_orig.jpg"
CODE_ORIG=f"{DIR}/dataobfuscator.py"

## Ouvrir le fichier image et extraire la taille pour calculer la taille maximale du code
def loadImage(path):
    with Image.open(path) as img:
        img.load()
    return img

img = loadImage(IMAGE_ORIG)
print(f"Image size: {img.size}")
max_code_size = math.floor(img.size[0]*img.size[1]/8)
print(f"Maximum code length: {max_code_size}")
################

## Ouvrir le fichier de code, le lire, et le compresser
def readCode(path):
    with open(path, "rb") as f:
        code = f.read()
    return code

def compress(string):
    compressed = zlib.compress(string)
    return compressed

def loadCode(path):
    code = readCode(path)
    print(f"Original code length: {len(code)}")
    code = compress(code)
    print(f"Compressed code length: {len(code)}")
    return code

code = loadCode(CODE_ORIG)
################

