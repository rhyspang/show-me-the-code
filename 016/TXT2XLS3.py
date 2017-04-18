#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-4-18 下午9:18
# @Author  : rhys
# @Software: PyCharm

import xlwt
import json
import os
from collections import OrderedDict

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def txt2xls3(filename, sheet_name):
    d = json.load(open(filename, 'r', encoding='utf-8'), object_pairs_hook=OrderedDict)
    wb = xlwt.Workbook()
    ws = wb.add_sheet(sheet_name)

    row = 0
    for item in d:
        col = 0
        for i in item:
            ws.write(row, col, i)
            col += 1
        row += 1
    wb.save(os.path.join(BASE_DIR, 'data/numbers.xls'))

if __name__ == '__main__':
    txt2xls3(os.path.join(BASE_DIR, 'data/numbers.txt'), 'numbers')