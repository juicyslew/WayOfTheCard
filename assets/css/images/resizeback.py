"""Makes an image bigger for me"""

from PIL import Image

if __name__ == '__main__':
    Im = Image.open("overlay1.png")
    Im = Im.resize((int(Im.size[0]*2.2), int(Im.size[1]*2.2)))
    Im = Im.save("overlay1.png")
