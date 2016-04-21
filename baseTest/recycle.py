#!/usr/bin/python
# -*- coding: utf-8 -*-

'this is a python demo'

__author__ = 'Wang Xiaoyang'

import sys
import types


def test() :
    args = sys.argv
    if len(args) == 1 :
        print 'hello %s !' % args
    elif len(args) == 2 :
        print 'hello %s !' % args[1]
    else :
        print 'Too manay argments'

if __name__ == '__main__':
    test()

print type('abc') == types.StringType

# for args in sys.path :
#     print args


age = 90
if age > 80:
    print 'age is %d' % age
else :
    print 'to small age'


names = ['zhangsan','lisi','wangwu']
index = 0;
for name in names :
    print 'name[%d] is %s' % (index,name)
    index = index + 1


x = 0;
sum = 0;
while x <= 100 :
    sum = sum + x;
    x = x + 1
print 'sum is %d ' % sum

dictTest = {'name':'Wangxiaoyang','age':27}
print dictTest['age']