#!/usr/bin/env python

import shutil, os, re
from PIL import Image
from wand.image import Image as wi
import pytesseract
import send2trash

old_dir = 'img_old'
new_dir = 'img_new'
tmp_dir = 'img_tmp'

if os.path.exists(old_dir) is not True:
    print('The "img_old" dir does not exist, please check.')

os.makedirs(new_dir, exist_ok=True)
os.makedirs(tmp_dir, exist_ok=True)

# A4 (1383, 979)
# box_size = (200, 50, 550, 100)
# left, top, right, bottom = (200, 50, 550, 100)
left, top, right, bottom = (830, 490, 1300, 650)

# images = os.listdir(old_dir)
# reg = re.compile('\w+\.(jpg|png)')
# images = reg.search(images).group()

reg_name = re.compile('(.+?)\.(pdf|jpg|png)')
# reg_code = re.compile('\d{10}')
reg_code = re.compile('\w{17}')

for old_img in os.listdir(old_dir):
    if reg_name.search(old_img) is not None:
        old_name = os.path.join(old_dir, old_img)
        try:
            # img = Image.open(old_name)

            with wi(filename=old_name, resolution=300) as pdf:
                # img = pdf.convert('jpeg')
                img = pdf.convert('png')
                img.crop(left, top, right, bottom)
                img.save(filename=os.path.join(tmp_dir, old_img.split('.')[0] + '_tmp.png'))


            # print(img.size)
            # img_resize = img.resize((1500, 800))
            # print(img_resize.size)
            # img_crop = img_resize.crop(box_size)

            img_crop = Image.open(os.path.join(tmp_dir, old_img.split('.')[0] + '_tmp.png'))
            text = pytesseract.image_to_string(img_crop).strip()
            text = reg_code.search(text).group()
            new_img = text + '.png'

            new_name = os.path.join(new_dir, new_img)

            print('----------' +
                  'Renaming "%s" to "%s"...' % (old_name, new_name) +
                  '----------')

            # shutil.move(old_name, new_name)
            shutil.copy(old_name, new_name)
        except IOError:
            print('The filetype of "%s" is not image.' % old_name)
        # except AttributeError:
            # print('The image "%s" has not been correctly cropped.' % old_name)
        else:
            pass
    else:
        pass

send2trash.send2trash(tmp_dir)
