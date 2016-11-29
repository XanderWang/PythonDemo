#!/usr/bin/python
#http://cn.python-requests.org/en/latest/user/quickstart.html
#-*- coding: utf-8 -*-
import requests
import traceback


url_base = 'http://192.168.'
s = requests.session()

for i in range(1,256,1):
    for j in range(1,256,1):
        try :
            url = "http://192.168.%s.%s/" % (i , j)
            print url
            r = s.get(url,timeout=1)
            print r
        except HTTPError ,e :
            print e

