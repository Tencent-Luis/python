#!/usr/bin/python
#-*- coding:utf-8 -*-
#依据cpu核心数，测试死循环
'''
启动与CPU核心数量相同的N个线程，在4核CPU上可以监控到CPU占用率仅有160%，也就是使用不到两核。
即使启动100个线程，使用率也就170%左右，仍然不到两核。
但是用C、C++或Java来改写相同的死循环，直接可以把全部核心跑满，4核就跑到400%，8核就跑到800%，为什么Python不行呢？
因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，
必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。
这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，
也只能用到1个核。
'''
import threading, multiprocessing

def loop():
	x = 0
	while True:
		x = x ^ 1

for i in range(multiprocessing.cpu_count()):
	t = threading.Thread(target = loop)
	t.start()