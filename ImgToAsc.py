#!/usr/bin/python3

from PIL import Image

GRAY_IMAGE_NAME = 'grayscale.png'

x_divider = 5
y_divider = 9

ascii_gray_scale_dict = {0 : '@',
                         1 : '#',
                         2 : '8',
                         3 : '&',
                         4 : 'o',
                         5 : ':',
                         6 : '*',
                         7 : '.',
                         8 : ' '}

img = Image.open('color.jpg').convert('LA')

# img.save(GRAY_IMAGE_NAME)

gray_img = Image.open(GRAY_IMAGE_NAME)

gray_band_gray_pixels = list(gray_img.getdata(0))

width, height = gray_img.size

ascii_pixels = [[0]* (int(width / x_divider) + 1) for _ in range(int(height / y_divider) + 1)]

for y in range(height):
    for x in range(width):
        ascii_pixels[int(y / y_divider)][int(x / x_divider)] += gray_band_gray_pixels[int(width*y + x)]

ascii_pixels = [list(map(lambda x: int(x / (x_divider * y_divider)), y)) for y in ascii_pixels]

with open("ascii_img.txt", "w") as f:
    for line in ascii_pixels:
        for gray in line:
            f.write(ascii_gray_scale_dict[int(gray / (255 / 8))])
            # f.write(' ')
        f.write('\n')
