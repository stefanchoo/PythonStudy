#!usr/bin/env python
# -*-coding:utf-8-*-

'''
工欲善其事，必先利其器！
运维：IT自动化
'''

# python 的文件处理
'''
r 以只读模式打开文件
w 以只写模式打开文件 || 没有创建，有则覆盖
a 以追加模式打开文件 || 在最后追加 一般是写在缓冲区中，需要调用flush写入

r+b 以读写模式打开
w+b 以写读模式打开
a+b 以追加及读模式打开
'''

# f = file('myfile.txt') # 默认是读模式
f = file('myfile.txt', 'r')
for line in f.readlines():
    # strip() 脱掉空格和换行符
    line = line.strip('\n').split(':')
    print line
f.close()

f = file('myfile.txt', 'a')
f.write("\n123")
f.flush()     # 需要 刷新一下缓存！

