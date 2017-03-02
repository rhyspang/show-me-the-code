# -*- coding: utf-8 -*-
# @Author: stoonejames
# @Date:   2016-11-27 12:19:51
# @Last Modified by:   stoonejames
# @Last Modified time: 2017-03-02 19:44:44


import re


def counting_words(file_name):
    text = open(file_name, 'r').read()
    words = re.findall(r'[\w\']+', text)
    words = map(lambda s: s.lower(), words)
    result = {}
    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    result = sorted(result.items(), key=lambda d: d[1], reverse=True)
    for a, b in result:
        print a, b


if __name__ == '__main__':
    counting_words('words.txt')
