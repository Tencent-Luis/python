#!/usr/bin/python
#-*- coding: utf-8 -*-
'a test module'
__author__ = "playcrab"
__date__ = "$2015-7-8 17:39:49$"

#导入模块
import sys

def test():
    args = sys.argv
    print args
    if len(args) == 1:
        print 'Hello, Python!'
    elif len(args) == 2:
        print 'Hello, %s!' % args[1]
    else:
        print 'Too many argments!'


#函数和变量作用域
def __private_1(name):   #私有函数，模块外无法访问
	return 'Hello, %s!' % name

def __private_2(name):
	return 'Hi, %s!' % name

def greeting(name):
	if len(name) > 3:
		return __private_1(name)
	else:
		return __private_2(name)


if __name__ == "__main__":
    test()