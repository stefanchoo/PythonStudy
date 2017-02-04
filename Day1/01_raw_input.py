#!/usr/bin/env python
#-*-coding:utf-8-*-

# raw_input() 默认都是字符串 
# input() 可以根据你输入的类型进行判断，就把它直接拿过来

#info = 'This is a variable'

name = raw_input('Please input your name:')

#age = raw_input('your age:')
#age = int(raw_input('your age:'))
age = input('your age:')

job = raw_input('your job:')
salary = input('your salary:')

'''
%d -> int
%f -> float
%s -> str
'''
print '''
-------------------------------
Personal information of %s:
		Name : %s
		Age : %d
		Job : %s
		Salary : %f
--------------------------------
''' %(name, name, age, job, salary)