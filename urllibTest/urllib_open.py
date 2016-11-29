#!/usr/bin/python
# http://cn.python-requests.org/en/latest/user/quickstart.html
# -*- coding: utf-8 -*-
import urllib
import urllib2

# request = urllib2.Request("http://www.baidu.com")

# response = urllib2.urlopen(request)

# print response.read().decode("utf-8")

# login csdn

agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
headers = {"User-Agent": agent}
values = {"username": "420640763@qq.com", "password": "xy19890318"}
data = urllib.urlencode(values)
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)
print response.read()
