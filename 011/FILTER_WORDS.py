#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-4-4 上午8:56
# @Author  : rhys
# @File    : FILTER_WORDS.py
# @Project : show-me-the-code
# @Software: PyCharm

import re


def filter_words(input_text):
    with open('./filtered_words.txt', 'r') as f:
        text = f.read()
        words_list = re.split('\s+', text)
        for words in words_list:
            if re.search(words, input_text):
                print(words)
                return True
    return False


if __name__ == '__main__':
    txt = input('text:')
    if filter_words(txt):
        print('Freedom')
    else:
        print('Human Rights')
