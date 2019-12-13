#!/usr/bin/env python

import shutil, os, re
from PIL import Image
import pytesseract

old_dir = 'img_old'
new_dir = 'img_new'

if os.path.exists(old_dir) is not True:
    print('The "img_old" dir does not exist, please check.')

os.makedirs(new_dir, exist_ok=True)

box_size = (280, 50, 500, 100)

for old_img in os.listdir(old_dir):
    old_name = os.path.join(old_dir, old_img)
    try:
        img = Image.open(old_name)
        img_crop = img.crop(box_size)
        text = pytesseract.image_to_string(img_crop).strip()
        new_img = text + '.png'

        new_name = os.path.join(new_dir, new_img)

        print('----------' +
              'Renaming "%s" to "%s"...' % (old_name, new_name) +
              '----------')

        # shutil.move(old_name, new_name)
        shutil.copy(old_name, new_name)
    except IOError:
        print('The filetype of "%s" is not image.' % old_name)
    else:
        pass


# fapiao = Image.open('img/fapiao.jpg')

# fapiao1 = fapiao.crop(box_size)

# fapiao1.save("img/fapiao1.jpg")

# text = pytesseract.image_to_string(fapiao1).strip()

# print(text)
