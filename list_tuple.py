#!/usr/bin/python
# -*- coding: utf-8 -*-

listDemo = ['I', 'am' , 27 ]
print 'listDemo : %s' % listDemo
print 'listDemo len %d' % len(listDemo)
endItem = raw_input('input to add to listDemo : ')
listDemo.append(endItem)
print 'after append'
print 'listDemo : %s' % listDemo
print 'listDemo len %d' % len(listDemo)
print 'after sort'
listDemo.sort()
print 'listDemo : %s' % listDemo
print 'listDemo len %d' % len(listDemo)
