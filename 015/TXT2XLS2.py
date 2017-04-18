# -*- coding: utf-8 -*-
# @Author: rhyspang
# @Date:   2017-04-18 19:33:09
# @Last Modified by:   rhyspang
# @Last Modified time: 2017-04-18 19:59:00

import xlwt
import json
import os
from collections import OrderedDict

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def txt2xls2(filename, sheet_name):
    d = json.load(open(filename, 'r', encoding='utf-8'), object_pairs_hook=OrderedDict)
    wb = xlwt.Workbook()
    ws = wb.add_sheet(sheet_name)
    row = 0
    for idx, city in d.items():
        ws.write(row, 0, idx)
        ws.write(row, 1, city)
        row += 1
    wb.save(os.path.join(BASE_DIR, 'data/student.xls'))


if __name__ == '__main__':
    filepath = os.path.join(BASE_DIR, 'data/student.txt')
    print(filepath)
    txt2xls2('data/student.txt', 'student')
