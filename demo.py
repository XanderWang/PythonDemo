#!/usr/bin/python
# -*- coding: utf-8 -*-
# print u'汪小阳'
# print 'please input you name'
# name = raw_input('Please input your name : ')
# print 'hello,%s' % name
listTest = ['hello','my','name','is',u'汪小阳']
print listTest
listTest.append(u'测试')
print 'after add item'
print listTest
listTest[-1] = 'last one'
print 'after change the last one'
print listTest

tupleTest = (1,'>',2,['is','right'])
print tupleTest
tupleTest[-1][0] = 0;
print tupleTest
