#!/usr/bin/python
#http://cn.python-requests.org/en/latest/user/quickstart.html
#-*- coding: utf-8 -*-
import requests
url_login = "http://www.heibanke.com/accounts/login"
url_form = "http://www.heibanke.com/lesson/crawler_ex03/"

def post_login(session, url, data):
  print 'stp 1',data
  session.get(url)
  params = {'csrfmiddlewaretoken':session.cookies.get('csrftoken')}
  print 'stp 2',params
  params.update(data)
  print 'stp 3',params,3
  print 'stp 4',data
  r = session.post(url, data=params)
  print 'url',r.url
  return r, session

s = requests.Session()
r,s = post_login(s,url_login,{'username':'test','password':'test123'})
print 'login',r.status_code
print '--------------------------------'
r = s.post(url_form)
print r.text