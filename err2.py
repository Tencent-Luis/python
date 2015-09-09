#!/usr/bin/env python
#-*- coding: utf-8 -*-
#pdb方式调试
#
import pdb

s = '0'
n = int(s)
pdb.set_trace()  #运行到这里自动暂停
print 10 / n