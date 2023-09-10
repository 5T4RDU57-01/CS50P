import os
import sys
from PIL import Image , ImageOps


def main():
    validation()

    image_overlay(sys.argv[1] , sys.argv[2])

def validation():
    if len(sys.argv) == 1:
        sys.exit('Too few command-line arguments')

    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')

    ext = ['png' , 'jpg' , 'jpeg']

    try:
        a = sys.argv[1].split('.')
        b = sys.argv[2].split('.')
    except:
        sys.exit('Invalid input')

    a[1] , b[1] = a[1].lower() , b[1].lower()

    if a[1] not in ext or b[1] not in ext:
        sys.exit('Invalid input')

    if a[1] != b[1]:
        sys.exit('Input and output have different extentions')


def image_overlay(input_img , output_img):
    shirt = Image.open('shirt.png')
    img_size = shirt.size
    try:
        img_one = Image.open(input_img)
    except FileNotFoundError:
        sys.exit('Input does not exist')

    img_one = ImageOps.fit(img_one , size=img_size)

    img_two = img_one.copy()
    img_two.paste(shirt , shirt)
    img_two.save(output_img)


if __name__ == '__main__':
    main()