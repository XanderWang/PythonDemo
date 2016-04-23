#!/usr/bin/python
# -*- coding:utf-8 -*-
'this is a network demo'
__author__ = 'wangxiaoyang'

import requests
base_url = 'http://www.baidu.com'
s = requests.session()
r = s.get(base_url)
print r.content