#!/usr/bin/env python
#-*- coding: utf-8 -*-
#name = raw_input('请输入你的名字：');
#print 'hello,',name;

#print r'''line1
#line2
#line3''';

#age = 5
#if age >= 18:
#	print 'your age is', age
#	print 'adult'
#elif age > 6:
#	print 'your age is', age
#	print 'teeager'
#else:
#	print 'your age is', age
#	print 'kid'

#sum = 0
#n = 99
#while n > 0:
#	sum = sum + n
#	n = n - 2
#print sum

birth = int(raw_input('请输入出生年份:'));
if birth < 2000:
	print '00前'
else:
	print '00后'