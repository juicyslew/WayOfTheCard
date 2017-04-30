"""Makes an image bigger for me"""

from PIL import Image

if __name__ == '__main__':
    Im = Image.open("overlay1.png")
    Im = Im.resize((int(Im.size[0]*1.25), int(Im.size[1]*1.25)))
    Im = Im.save("overlay1.png")
