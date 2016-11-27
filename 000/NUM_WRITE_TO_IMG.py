# -*- coding: utf-8 -*-
# @Author: rhys
# @Date:   2016-11-07 21:28:14
# @Last Modified by:   rhys
# @Last Modified time: 2016-11-08 15:28:42


from PIL import Image, ImageDraw, ImageFont

IMG_URL = './images.jpg'
FONT_URL = './Roboto-Italic.ttf'
FONT_SIZE = 50
TEXT = '12'
PADDING_RIGHT,  PADDING_TOP= 20, 20
FILL = '#FF0000'

RESULT_IMG_NAME = 'result.jpg'


if __name__ == '__main__':
	img = Image.open(IMG_URL)
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype(FONT_URL, size=FONT_SIZE)
	img_w, img_h = img.size
	font_w, font_h = font.getsize(TEXT)
	x, y = img_w - PADDING_RIGHT - font_w, PADDING_TOP
	draw.text((x, y), TEXT, fill=FILL, font=font)
	img.save(RESULT_IMG_NAME, 'jpeg')