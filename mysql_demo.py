#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Created on Mar 27 2017
@author: pavle

This script shows basic use of mysql database.
"""

import MySQLdb as db



my_db = db.connect('127.0.0.1', 'root', 'xxx', 'hr_tencent')
cursor = my_db.cursor()
cursor.execute("SET NAMES utf8")

cursor.execute("drop table if exists algrithm_engineer")

#set character encoding mode as utf8 to insert Chinese
sql_create = """create table algrithm_engineer (date date, job_title char(50) not null, 
	number tinyint, location char(10), job_description varchar(500)) 
	DEFAULT CHARSET utf8 COLLATE utf8_general_ci"""

cursor.execute(sql_create)

sql_insert = '''insert into algrithm_engineer (date, job_title, number, location, job_description) 
	value ('2017-04-20', '测试11121', '2', 'shanghai', 'aaaaaa')'''
cursor.execute(sql_insert)
my_db.commit()
cursor.execute('select * from algrithm_engineer')
data = cursor.fetchone()
print data
my_db.close()