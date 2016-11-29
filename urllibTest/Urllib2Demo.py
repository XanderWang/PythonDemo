#!/usr/bin/python
# -*- coding: utf-8 -*-
'this is a demo for urllib2'

import urllib2

response = urllib2.urlopen('http://app.mi.com/topList')
html = response.read()
print  html