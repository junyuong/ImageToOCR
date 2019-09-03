from tkinter.simpledialog import *
from pytesseract import *
import glob
from PIL import Image

def main():
    multiImage = glob.glob('*.jpg')
    for i in multiImage:
        print(i)
        image = Image.open(i)
        text = image_to_string(image, lang="kor+eng")
        file = open(i+'.txt', 'w', encoding='utf8')
        file.write(text)
        file.close()

if __name__ == "__main__":
    main()