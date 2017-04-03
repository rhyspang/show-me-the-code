#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-4-3 上午9:15
# @Author  : rhys
# @File    : VERIFICATION_CODE.py
# @Project : show-me-the-code
# @Software: PyCharm

import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter


def random_color():
    """
    :return: 返回随机颜色
    """
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def verification_code(chars=string.ascii_letters+string.digits,
                      code_len=4,
                      size=(400, 250)):
    """
    生成验证码， 每个字符创建一个图片对象，将其随机旋转一定角度后粘贴到验证码图片对象上
    :param chars: 备选字符集，默认为大小写字母和数字集合
    :param code_len: 验证码长度   
    :param size: 验证码图片尺寸
    :return: 返回验证码图片对象和验证码
    """
    # 随机生成验证码
    code = ''.join(random.sample(chars, code_len))
    # 验证码图片对象
    code_img = Image.new('RGBA', size, (255, 255, 255))
    # 验证码图片画笔对象
    code_draw = ImageDraw.Draw(code_img)
    # 字体对象
    font = ImageFont.truetype('./XXRaytid.ttf', size[0] // 4)
    font_width, font_height = font.getsize(code)
    font_start_x, font_start_y = size[0] - font_width >> 1, size[1] - font_height >> 1
    # 调整起始坐标(对随机字符间隔进行估计)
    font_start_x -= 60
    font_start_y -= 40
    # 单个字符图片的内边距
    item_padding = 20
    for i in range(code_len):
        item_width, item_height = font.getsize(code[i])
        item_img = Image.new('RGBA', (item_width+(item_padding << 1),
                                      item_height+(item_padding << 1)),
                             (255, 255, 255, 0))
        item_draw = ImageDraw.Draw(item_img)
        item_draw.text((20, 20), code[i], random_color(), font)
        item_img = item_img.rotate(random.randint(-30, 30))
        interval = random.randint(10, 40)
        code_img.paste(item_img, (font_start_x, font_start_y), mask=item_img)
        # 偏移一个10到40的随机距离加上该字符宽度
        font_start_x += interval + item_width

    # print(code)

    for x in range(size[0]):
        for y in range(size[1]):
            dot = code_img.getpixel((x, y))
            if dot == (255, 255, 255, 255) or dot == (0, 0, 0, 0):
                code_draw.point((x, y), fill=random_color())
        # 模糊化

    code_img = code_img.filter(ImageFilter.BLUR)
    code_img.save('./verification_code.png', 'PNG')
    return code_img, code


if __name__ == "__main__":
    verification_code()
