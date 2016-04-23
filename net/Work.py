#!/usr/bin/python
#http://cn.python-requests.org/en/latest/user/quickstart.html
#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


url_base = 'http://www.woshipm.com/'
# url_base = 'http://cn.python-requests.org/en/latest/user/quickstart.html'
s = requests.session()
r = s.get(url_base)

print r
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
for divs in soup.find_all('ul') :
    print '*****************************************************'
    print index
    index += 1
    clazzList = divs.get('class')
    if( None == clazzList ) :
        continue
    if( len(clazzList) <=0 ) :
        continue
    print '  len',len(clazzList),' , and first class =',clazzList[0],' , and cmp',clazzList[0] == 'sub-menu'
    if( clazzList[0]=='sub-menu' ):
        allUrl = divs.find_all('a')
        for url in allUrl :
            print '    ',url.text,url.get('href')
        print '------------------------------------------------------'
# for alink in soup.div.div.find_all('a') :
#     print alink
