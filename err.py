#!/usr/bin/env python
#-*- coding: utf-8 -*-
#断言方式调试
#
#def foo(s):
#	n = int(s)
#	assert n != 0, 'n is zero!'
#	return 10 / n
#
#def main():
#	foo('0')
#
#main()


#logging方式调试
#
import logging
logging.basicConfig(level=logging.DEBUG)

s = '0'
n = int(s)
logging.debug('n = %d' % n)
print 10 / n