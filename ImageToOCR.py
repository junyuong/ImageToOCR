from tkinter.simpledialog import *
from pytesseract import *
import glob
from PIL import Image

def getOCR(multiImage):
    if multiImage:
        for i in multiImage:
            print("Image 로딩중 : " + i)
            image = Image.open(i)
            text = image_to_string(image, lang="kor+eng")
            file = open(i + '.txt', 'w', encoding='utf8')
            file.write(text)
            file.close()

def main():
    jpgImage = glob.glob('*.jpg')
    bmpImage = glob.glob('*.bmp')
    pngImage = glob.glob('*.png')
    getOCR(jpgImage)
    getOCR(bmpImage)
    getOCR(pngImage)
    print("OCR 변환 완료")
if __name__ == "__main__":
    main()