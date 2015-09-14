#!/usr/bin/python
#-*- coding:utf-8 -*-
#锁的应用
import time, threading

#假定这是存款:
blance = 0
lock = threading.Lock()

def change_it(n):
	#先存后取，(正常执行的情况下)结果应该为0:
	#但t1,t2如果交替执行的话，结果就未必是0:
	global blance
	blance = blance + n  #x = blance + n   blance = x
	blance = blance - n  #x = blance - n   blance = x

def run_thread(n):
	for i in range(100000):
		#先获得锁
		lock.acquire()
		try:
			change_it(n)
		finally:
			#改完一定要释放锁
			lock.release()

t1 = threading.Thread(target = run_thread, args = (5,))
t2 = threading.Thread(target = run_thread, args = (8,))
t1.start()
t2.start()
t1.join()
t2.join()
print blance