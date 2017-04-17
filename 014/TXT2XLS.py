#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-4-17 下午7:26
# @Author  : rhys
# @File    : TXT2XLS.py
# @Project : show-me-the-code
# @Software: PyCharm

import xlwt
import json
from collections import OrderedDict


def txt2xls(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        students_dict = json.load(f, object_pairs_hook=OrderedDict)
        wb = xlwt.Workbook()
        ws = wb.add_sheet('student')

        row = 0
        for k, v in students_dict.items():
            ws.write(row, 0, k)
            col = 1
            for item in v:
                ws.write(row, col, item)
                col += 1
            row += 1
    wb.save('data/student.xls')

if __name__ == '__main__':
    txt2xls('data/student.txt')
