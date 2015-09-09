#!/usr/bin/env python
#-*- coding: utf-8 -*-
#导入MySQL驱动:
import mysql.connector

conn = mysql.connector.connect(user = 'root', password = '123456', database = 'test', use_unicode = True)
cursor = conn.cursor()

#创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
#插入记录
cursor.execute('insert into user (id, `name`) values (%s, %s)', ['1', 'Michael'])
total = cursor.rowcount
print '成功插入记录数：' + str(total)

#提交事务：
conn.commit()
cursor.close()

#运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ['1'])
values = cursor.fetchall()
print values

#关闭cursor和connection
result = cursor.close()
print result
conn.close()
