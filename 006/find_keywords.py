# -*- coding: utf-8 -*-
# @Author: stoonejames
# @Date:   2017-03-02 19:51:15
# @Last Modified by:   stoonejames
# @Last Modified time: 2017-03-02 21:13:16

import os
import re
from collections import Counter

DIR = 'DAIRY' + os.sep
FILTED_WORDS = ['a', 'an', 'am', 'i', 'he', 'she', 'him', 'his',
                'my', 'her', 'those', 'that', 'this', 'they', 'of',
                'to', 'of', 'the', 'was', 'would', 'and', 'for', 'in',
                'could', 'he', 'on', 'in', 'had', '\'', 'me']


def get_all_files(dir):
    files_in_dir = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            files_in_dir.append(os.path.join(root, file))
    print files_in_dir
    return files_in_dir


def count_keywords(file):
    with open(file, 'r') as f:
        words = re.findall(r'[\w\']+', f.read())
    words_lowercase_filted = filter(
        lambda s: s.lower() not in FILTED_WORDS, words)
    counter = Counter(words_lowercase_filted)
    return counter.most_common(5)


def main():
    for file in get_all_files(DIR):
        print count_keywords(file)


if __name__ == "__main__":
    main()
