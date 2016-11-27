# -*- coding: utf-8 -*-
# @Author: stoonejames
# @Date:   2016-11-27 17:17:35
# @Last Modified by:   stoonejames
# @Last Modified time: 2016-11-27 17:53:46

import Image
import imghdr
import os

TO_SIZE = (640, 1136)
SUB_FOLDER = r'resized_pics/'


def resize_img(img_name):
    detail_img_name = img_name.split('.')
    print detail_img_name
    img = Image.open(img_name)
    if img.size != TO_SIZE:
        resized_img = img.resize(TO_SIZE, Image.ANTIALIAS)
    resized_img.save(
        SUB_FOLDER + detail_img_name[0] + '_resized' + '.' + detail_img_name[1])

if __name__ == '__main__':
    if not os.path.exists(SUB_FOLDER):
        os.mkdir(SUB_FOLDER)

    files = filter(os.path.isfile, os.listdir('.'))
    imgs = filter(imghdr.what, files)
    for img in imgs:
        resize_img(img)
