#!/usr/bin/python
# -*- coding: utf-8 -*-
for x in range(1,10) :
    print "------ start x = %d ------" % x
    for y in range(1,10) :
        print "x = %d , y = %d" % (x ,y)
        if y == 3 :
            print "break y"
            break
    if x == 3 :
        print "break x"
        break
