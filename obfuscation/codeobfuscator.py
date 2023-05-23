from PIL import Image
import os,math
import zlib
from bitstring import BitArray

DIR = os.path.dirname(os.path.realpath(__file__))
IMAGE_ORIG=f"{DIR}/image_orig.jpg"
IMAGE_STEG=f"{DIR}/image_stega.jpg"
CODE_ORIG=f"{DIR}/dataobfuscator.py"
LSB_PAYLOAD_LENGTH_BITS = 32

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

## Valider que la taille du code compressé est inférieure à la tailla maximale permise
if len(code) > max_code_size:
    raise Exception("Code size cannot be greather than image size")
################

## Utiliser le code d’obfuscation pour mettre le code dans l’image
def obfuscate_via_lsb(data, img):
    data = BitArray(uint=len(data) * 8, length=LSB_PAYLOAD_LENGTH_BITS).bin + BitArray(bytes=data).bin

    i = 0
    try:
        width, height = img.size
        if len(data) > width * height * 3:
            print("Data is too large to be embedded in the image. Data contains {} bytes, maximum is {}".format(
                int(len(data) / 8), int(width * height * 3 / 8)))
            exit(1)
        for x in range(0, width):
            for y in range(0, height):
                pixel = list(img.getpixel((x, y)))
                for n in range(0, 3):
                    if i < len(data):
                        pixel[n] = pixel[n] & ~1 | int(data[i])
                        i += 1
                img.putpixel((x, y), tuple(pixel))
                if i >= len(data):
                    break
            if i >= len(data):
                break
        return img
    except IOError:
        # print("Could not open {}. Check that the file exists and it is a valid image file.".format(input_file))
        exit(1)

obfuscate_via_lsb(code, img)
################

## Sauvegarder le résultat dans une nouvelle image JPG
img.save(IMAGE_STEG)
################