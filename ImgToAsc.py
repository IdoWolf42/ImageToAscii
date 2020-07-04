#!/usr/bin/python3

from PIL import Image

GRAY_IMAGE_NAME = 'grayscale.png'

ascii_gray_scale_dict = {1 : '@',
                         2 : '#',
                         3 : '8',
                         4 : '&',
                         5 : 'o',
                         6 : ':',
                         7 : '*',
                         8 : '.',
                         9 : ' '}

img = Image.open('color.jpg').convert('LA')

img.save(GRAY_IMAGE_NAME)

gray_img = Image.open(GRAY_IMAGE_NAME)
