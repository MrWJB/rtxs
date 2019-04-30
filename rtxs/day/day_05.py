#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json
import os
from multiprocessing import Process

# class Student(object):
#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score
#
# def object2dict(std):
#     return {
#         'name': std.name,
#         'age':std.age,
#         'score':std.score
#     }
#
# s = Student('zhangsan', 22, 2000)
# print(json.dumps(s, default=object2dict))

###########################多进程、多线程

# print('Process (%s) start...' % os.getpid())

# Only works on Unix/Linux/Mac:
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(),os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


# 多进程
# 子进程要执行的代码
# def run_process(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))
#
# #join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_process, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')


# Pool进程池 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
from multiprocessing import Pool
import os, time, random

# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start= time.time()
#     time.sleep(random.random()*3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))
#
#
# if __name__ == '__main__':
#     print('Parent process %s.' %(os.getpid()))
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')


import subprocess

print('$ nslookup  www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)
