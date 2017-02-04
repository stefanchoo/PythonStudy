#!/usr/bin/env python
#-*-coding:utf-8-*-

# 注意编程风格，要进行缩进
# python解释器会再正在执行之前，先检查

def main():
	print 'hello'

main()

print '+++++++'

# 常量一般使用大写来描述
PI = 3.1415926
print PI

x = 2
y = 3
z = x
x = 5

print x
print id(x) 

print y
print id(z)

print x + y

