#!/usr/bin/python
#-*- coding:utf-8 -*-
''''''
多重继承
''''''
class Animal(object):
	pass

class Mammal(Animal):
	pass

class Bird(Animal):
	pass

class Dog(Mammal, RunableMixin, CarnivorousMixin):
	pass

class Bat(Mammal, FlyableMixin):
	pass

class Parrot(Bird):
	pass

class Ostrich(Bird, RunableMixin):
	pass



#多重继承，Mixin设计，目的是为一个类添加多个功能
class RunableMixin(object):
	def run(self):
		print 'Running....'

class FlyableMixin(object):
	def fly(self):
		print 'Flying....'

#肉食动物类
class CarnivorousMixin(object):
	pass

#植食动物类
class HerbivoresMixin(object):
	pass

