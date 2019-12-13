#!/usr/bin/env python

from PIL import Image
import pytesseract

fapiao = Image.open('fapiao.jpg')

fapiao1 = fapiao.crop((280,50,500,100))

fapiao1.save("fapiao1.jpg")

text = pytesseract.image_to_string(fapiao1).strip()

print(text)
