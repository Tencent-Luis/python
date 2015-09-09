#!/usr/bin/python
#-*- coding: utf-8 --*--
import math
import hello

#函数定义
def my_abs(x):
	if not isinstance(x, (int, float)):   #检查参数数据类型
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x

#定义空函数
def nop():
	pass

#函数返回多个值(其实就是返回一个元组)
def move(x, y, step, angle = 0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny

#定义函数默认参数
#计算指定数的任意次幂
def power(x, n = 2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s

def enroll(name, gender, age = 6, city = 'BJ'):
	print 'name:', name
	print 'gender:', gender
	print 'age:', age
	print 'city:', city
	return

def add_end(L = None):
	if L is None:
		L = []
	L.append('END')
	return L

#定义可变参数函数
#调用此函数时，需先组装出list或元组(tuple)
def cacl(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum

#定义关键字参数
def person(name, age, **kw):
	print 'name:', name, 'age:', age, 'other:', kw

#参数组合
#参数定义顺序：必选参数，默认参数，可变参数，关键字参数
def func(a, b, c = 0, *args, **kw):
	print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw

#递归函数
#def fact(n):
#	if n == 1:
#		return 1
#	return n * fact(n - 1)
#实现尾递归
#尾递归：在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
def fact(n):
	return fact_iter(n, 1)

def fact_iter(num, product):
	if num == 1:
		return product
	return fact_iter(num - 1, num * product)





#x, y = move(100, 100, 60, math.pi / 6)
#r = move(100, 100, 60, math.pi / 6)
#print enroll('Jack', 'F', city = 'GZ')
#传入可变参数
#nums = [5,6,7]
#print cacl(*nums)

#传入关键字参数
#kw = {'city': 'GuangZhou', 'job': 'Doctor', 'address': 'sport chang'}
#person('Jack', 30, gender = 'F', **kw)

#参数组合
#args = (5, 8, 6, 8)
#kw = {'val': 100}
#func(1, 2, 4, 'a', 'b', x = 99)
#func(*args, **kw)

#调用递归函数
#print fact(6)

#调用模块函数
print hello.greeting('Lu')