#!/usr/bin/env python
# -*-coding:utf-8-*-

import sys

accounts_filename = 'accounts.txt'
accounts_lock_filename = 'accounts_lock.txt'

retry_limit = 3
retry_count = 0

print 'Remember you only have %d shots \n' % retry_limit

while retry_count < retry_limit:
    username = raw_input('Please input your username : ')
    lock_check = file('accounts_lock.txt')           # 输入用户名之后可以先检查是否在黑名单中

    for line in lock_check.readlines():              # 循环lock 文件
        line = line.split()
        for i in range(len(line)):
            if line[i] == username:
                sys.exit('很抱歉，您的用户名已经被锁定！')
            i += 1
    password = raw_input('Please input your password : ')
    f = file(accounts_filename, 'r+')                #打开帐号文件
    match_flag = False                               # 默认为Flase,如果用户match 上了，就设置为 True
    for line in f.readlines():
        usr, passwd = line.strip('\n').split(':')
        if usr == username and passwd == password:
            print 'Match!', username
            match_flag = True                        #相等就把循环外的match_flag变量改为了True
            break                                    #然后就不用继续循环了，直接 跳出，因为已经match上了
    f.close()
    if not match_flag:
        print 'User Unmatched'
        retry_count += 1
        if retry_limit - retry_count != 0:
            print 'you have %d shots \n' % (retry_limit - retry_count)
    else:
        print 'Welcome to Stefan Learning System'
        break

else:
    print 'Your account is locked!'
    f = file(accounts_lock_filename, 'a+')
    f.write(username + ' ')
    f.close()


