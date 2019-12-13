#!/usr/bin/env python

import shutil, os, re
from PIL import Image
import pytesseract
import send2trash

old_dir = 'img_old'
new_dir = 'img_new'
tmp_dir = 'img_tmp'

if os.path.exists(old_dir) is not True:
    print('The "img_old" dir does not exist, please check.')

os.makedirs(new_dir, exist_ok=True)
os.makedirs(tmp_dir, exist_ok=True)

box_size = (200, 50, 550, 100)

for old_img in os.listdir(old_dir):
    old_name = os.path.join(old_dir, old_img)
    try:
        img = Image.open(old_name)
        # print(img.size)
        img = img.resize((1500,800))
        # print(img.size)
        img_crop = img.crop(box_size)
        img_crop.save(os.path.join(tmp_dir, old_img.split('.')[0] + '_tmp.png'))
        text = pytesseract.image_to_string(img_crop).strip()
        reg = re.compile('\d{10}')
        text = reg.search(text).group()
        new_img = text + '.png'

        new_name = os.path.join(new_dir, new_img)

        print('----------' +
              'Renaming "%s" to "%s"...' % (old_name, new_name) +
              '----------')

        # shutil.move(old_name, new_name)
        shutil.copy(old_name, new_name)
    except IOError:
        print('The filetype of "%s" is not image.' % old_name)
    except AttributeError:
        print('The image "%s" has not been correctly cropped.' % old_name)
    else:
        pass

send2trash.send2trash(tmp_dir)

# fapiao = Image.open('img/fapiao.jpg')

# fapiao1 = fapiao.crop(box_size)

# fapiao1.save("img/fapiao1.jpg")

# text = pytesseract.image_to_string(fapiao1).strip()

# print(text)
