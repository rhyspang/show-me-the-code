# -*- coding: utf-8 -*-
# @Author: stoonejames
# @Date:   2016-11-27 12:52:39
# @Last Modified by:   stoonejames
# @Last Modified time: 2016-11-27 16:58:01

import os
import re


BASE_DIR = os.path.abspath('.')
REG = r'\d{3}'
dirlist = os.listdir('.')
pattern = re.compile(REG)


dirs = filter(os.path.isdir, dirlist)
dirs.sort()
print dirs

for d in dirs:
    if pattern.match(d):
        os.rename(d, '%03d' % (int(d)))
