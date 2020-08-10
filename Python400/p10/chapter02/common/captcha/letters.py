#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random
import string

from PIL import Image, ImageDraw, ImageFont, ImageFilter


def random_text(length=4):
    """
    return a string, each char is an random ascii letter
    :param length: length of the string
    :return: random string
    """
    return ''.join(random.choices(string.ascii_letters, k=length))


def random_rgb():
    """
    random return an RGB color
    :return: random r, g, b range(0, 256)
    """
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def gen_code(length=4, size=(160, 40), font=('fonts/segoescb', 38)):
    # create Image object
    image = Image.new('RGB', size, (255, 255, 255))

    # create Font object
    ft = ImageFont.truetype(*font)

    # create Draw object and draw random
    draw = ImageDraw.Draw(image)
    for x in range(0, size[0], 2):
        for y in range(0, size[1]):
            draw.point((x, y), fill=random_rgb())

    # create letters
    code = random_text(length)

    # draw text
    for i in range(length):
        draw.text((40 * i +5, -5), code[i], random_rgb(), ft)

    # image = image.filter(ImageFilter.BLUR)
    return image, code


if __name__ == '__main__':
    image, code = gen_code()
    with open('test.jpg', 'wb') as img:
        image.save(img)
    print(code)
