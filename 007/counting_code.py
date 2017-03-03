
# -*- coding: utf-8 -*-
# @Author: stoonejames
# @Date:   2017-03-02 21:18:41
# @Last Modified by:   stoonejames
# @Last Modified time: 2017-03-03 09:38:29


'''
TODO
'''

import os
import re

DIR = 'dir' + os.sep
CODE_FILE_SUFFIXES = ['.c', '.cpp', '.py', '.java', '.js', '.html', '.css']
result = {}


def init():
    for i in CODE_FILE_SUFFIXES:
        result[i] = [0, 0, 0]


def counting_code_in_file(filename):
    pass


def main():
    init()
    for root, dirs, files in os.walk(DIR):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.splitext(file_path)[1] in CODE_FILE_SUFFIXES:
                counting_code_in_file(file_path)

if __name__ == '__main__':
    main()
