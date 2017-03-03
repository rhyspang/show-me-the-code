# -*- coding: utf-8 -*-
# @Author: stoonejames
# @Date:   2017-03-03 09:39:36
# @Last Modified by:   stoonejames
# @Last Modified time: 2017-03-03 09:45:46

from goose import Goose
from goose.text import StopWordsChinese
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

URL = 'http://www.ruanyifeng.com/blog/2015/05/thunk.html'


def extract(url):
    g = Goose({'stopwords_class': StopWordsChinese})
    article = g.extract(url=URL)
    return article.cleaned_text


def main():
    print extract(URL)

if __name__ == '__main__':
    main()
