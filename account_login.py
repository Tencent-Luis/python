#/usr/bin/python
#coding=utf-8
import urllib3
import base64
import time
import threading

from queue_config import master_host, author_login
from RedisQueue import RedisQueue

redis_conn = {'host': master_host[0] ,'port':master_host[1]}

q = RedisQueue('account_login', **redis_conn)
http = urllib3.PoolManager(num_pools=50)

def worker(value):
    params = {}
    params['account_login'] = base64.encodestring(value)
    r = http.request('POST', author_login, params)

    #服务器失败，重新压回队列
    if r.status != 200:
        q.put(value)

    #IP白名单验证失败，重新压回队列
    if r.data['status'] == 10002:
        q.put(value)
    print r.data

while 1:
    # time.sleep(1);
    if q.empty():
        print 'empty queue'
        break

    s = q.qsize()
    for i in range(0,s):
        value = q.get()
        t = threading.Thread(target=worker, args=(value,))
        t.start()
        if threading.active_count() >= 500:
            time.sleep(1)