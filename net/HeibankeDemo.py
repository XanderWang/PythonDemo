#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re

baseUrl_0 = 'http://www.heibanke.com/lesson/crawler_ex00/'
netSession = requests.session()
url = baseUrl_0
numRe = re.compile(r'[^\d<]*?(\d+)[^\d<]*?')
# numRe = re.compile(r'<h3>[\D<]*?(\d+).</h3>')
# numRe = re.compile(r'(\d+)')
# numStr = re.search(numRe, html)
# print numStr.group()
while False :
    print 'find url',url
    html = netSession.get(url).text
    soup = BeautifulSoup(html)
    numStr = re.findall(numRe,soup.h3.string)
    if len(numStr) == 0 :
        break
    else:
        url = baseUrl_0 + numStr[0]
# print url


baseUrl_1 = "http://www.heibanke.com/lesson/crawler_ex01/"

r = netSession.get(baseUrl_1)

print r.text
