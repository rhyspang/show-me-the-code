#!/usr/bin/bash python

from bs4 import BeautifulSoup
import urllib.request

URL = 'http://www.ruanyifeng.com/blog/2015/05/co.html'


def find_href(url):

    proto, rest = urllib.request.splittype(url)
    domain = urllib.request.splithost(rest)[0]
    with urllib.request.urlopen(url=url) as response:
        html = response.read()
        a_list = BeautifulSoup(html, 'html.parser').findAll('a')
        links = [a.get("href") for a in a_list]
        links = map(lambda a: proto + '://' + domain + a if a.startswith('/') or a.startswith('?') else a, links)
        return links

if __name__ == '__main__':
    result = find_href('http://pangsheng.me')
    for link in result:
        print(link)