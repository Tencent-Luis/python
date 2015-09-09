#!/usr/bin/python
#-*- coding:utf-8 -*-

class Animal(object):
	def run(self):
		print 'Animal is running...'


class Dog(Animal):
	def run(self):
		print 'Dog is running...'

	def eat(self):
		print 'Eat meat...'


class Cat(Animal):
	def run(self):
		print 'Cat is running...'


class Tortoise(Animal):
	def run(self):
		print 'Tortoise is running slowly...'



def run_twice(animal):
	animal.run()
	animal.run()



animal = Animal()
animal.run()

dog = Dog()
dog.run()
dog.eat()

cat = Cat()
cat.run()

print isinstance(dog, Dog)
print isinstance(cat, Cat)
print isinstance(dog, Animal)
print isinstance(animal, Cat)

run_twice(Tortoise())
print type(animal)