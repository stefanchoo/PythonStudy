#!/usr/bin/env python
#-*-coding:utf-8-*-

# raw_input() 默认都是字符串 
# input() 可以根据你输入的类型进行判断，就把它直接拿过来

#info = 'This is a variable'

name = raw_input('Please input your name:')

#age = raw_input('your age:')
#age = int(raw_input('your age:'))
#age = input('your age:')

job = raw_input('your job:')
salary = input('your salary:')


for i in range(10):
	age = input('age : ')
	if age > 40:
		msg = 'You are too fucking old!'
	elif age > 30:
		msg = 'You still have a few years to hook up.'
	elif age == 24:
		# shell 中打印会出现红色加粗
		msg = '\031[32;1mGOOD! 10 RMB!\031[0m' 
		break
	else:
		msg = 'You are still quite young, go hook up girls or boys'
	
	print msg
	print 'You still got %s shots!' % (9 - i)
print '''
%s
-------------------------------
Personal information of %s:
		Name : %s
		Age : %d
		Job : %s
		Salary : %f
--------------------------------
''' %(msg, name, name, age, job, salary)

'''
%d -> int
%f -> float
%s -> str
'''