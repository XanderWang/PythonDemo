#!/usr/bin/python
#http://cn.python-requests.org/en/latest/user/quickstart.html
#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


url_base = 'http://www.woshipm.com/'
# url_base = 'http://cn.python-requests.org/en/latest/user/quickstart.html'
s = requests.session()
r = s.get(url_base)

# print r.content
# print '--------------------------------'
print r.encoding
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text)
print soup.title
print soup.title.name
print soup.title.string

# for image in soup.find_all('img') :
#     print image.get('src')
index = 1
for divs in soup.find_all('div') :
    print index
    index += 1
    clazzList = divs.get('class')
    if( None == clazzList ) :
        continue;
    print clazzList
    if( len( clazzList ) > 0 & cmp( clazzList[0],'sub-menu' ) == 0):
        print divs
    print '==========================================='
# for alink in soup.div.div.find_all('a') :
#     print alink
