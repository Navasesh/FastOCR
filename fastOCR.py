#!/usr/bin/env python

import shutil, os, re
from PIL import Image
import pytesseract

fapiao = Image.open('img/fapiao.jpg')

box_size = (280,50,500,100)
fapiao1 = fapiao.crop(box_size)

fapiao1.save("img/fapiao1.jpg")

text = pytesseract.image_to_string(fapiao1).strip()

print(text)
