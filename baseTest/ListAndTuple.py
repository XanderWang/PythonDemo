#!/usr/bin/python
# -*- coding: utf-8 -*-
print 'Now, let\'s test the List and Tuple'
listDemo = ['I', 'am' , 27 ]
print 'list : %s' % listDemo
print 'list len = %d' % len(listDemo)
addItem = raw_input('input an item to add the list : ')
listDemo.append(addItem)
print 'after append'
print 'list : %s' % listDemo
print 'list len = %d' % len(listDemo)
print 'let\'s test sort'
print 'after sort'
listDemo.sort()
print 'list : %s' % listDemo
print 'listDemo len = %d' % len(listDemo)

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
