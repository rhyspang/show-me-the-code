#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-4-4 上午9:46
# @Author  : rhys
# @File    : FILTER_WORDS_PLUS.py
# @Project : show-me-the-code
# @Software: PyCharm

import re


def read_keywords(filename):
    with open(filename, 'r') as f:
        text = f.read()
        words_list = re.split('\s+', text)
        return words_list


def filter_words(input_text):
    words_list = read_keywords('./filtered_words.txt')
    for words in words_list:
        input_text = re.sub(words, len(words)*'*', input_text)
    return input_text


if __name__ == '__main__':
    print(filter_words(input('text:')))
