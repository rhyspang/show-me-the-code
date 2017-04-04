#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-4-4 上午10:33
# @Author  : rhys
# @File    : TIEBAR_SPIDER.py
# @Project : show-me-the-code
# @Software: PyCharm

import requests
import os
from bs4 import BeautifulSoup


class TieBarSpider(object):
    def __init__(self, url, path='./'):
        self.url = url
        self.path = path

    def retrieve(self):
        # try:
        #     os.mkdir('imgs')
        # except:
        #     raise FileExistsError('imgs文件夹已存在')
        if not os.path.exists('./imgs'):
            os.mkdir('imgs')
        self._run()

    def _run(self):
        response = requests.get(self.url)
        bs = BeautifulSoup(response.text, 'html.parser')
        results = bs.find_all('img', pic_type="0")
        maxn = len(results)
        for i in range(maxn):
            self._save_pic(results[i]['src'], '%03d.jpg' % i)

    def _save_pic(self, url, filename):
        pic = requests.get(url)
        with open(os.path.join(os.path.join(self.path, 'imgs'), filename), 'ab') as f:
            print('saving', filename)
            f.write(pic.content)


if __name__ == '__main__':
    spider = TieBarSpider(url="http://tieba.baidu.com/p/2166231880")
    spider.retrieve()
