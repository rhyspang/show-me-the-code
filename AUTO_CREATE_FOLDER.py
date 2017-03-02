# -*- coding: utf-8 -*-
# @Author: stoonejames
# @Date:   2016-11-27 16:54:47
# @Last Modified by:   stoonejames
# @Last Modified time: 2017-03-02 19:46:05

import os
import re

PATTERN = r'\d{3}'

if __name__ == "__main__":
    items = os.listdir('.')
    dirs = filter(os.path.isdir, items)
    print dirs

    maxn = 0
    for dir in dirs:
        maxn = int(dir) if re.match(PATTERN, dir) and int(dir) > maxn else maxn

    os.mkdir('%03d' % (maxn+1))
