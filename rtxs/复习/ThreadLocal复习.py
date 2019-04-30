#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading


# 在多线程环境下，每个线程都有自己的数据。一个线程使用自己的局部变量比使用全局变量好，因为局部变量只有线程自己能看见，不会影响其他线程，而全局变量的修改必须加锁。
# 但是局部变量也有问题，就是在函数调用的时候，传递起来很麻烦：

class Student(object):
    def __init__(self, name):
        self.name = name


global_dict = {}


def std_thread(name):
    std = Student(name)
    # 把std放到全局变量global_dict中：
    global_dict[threading.current_thread().getName()] = std
    do_task_1()
    do_task_2()


def do_task_1():
    # pass
    # 不传入std, 而是根据当前线程查找
    std = global_dict[threading.current_thread().getName()]


def do_task_2():
    # pass
    # 不传入std, 而是根据当前线程查找
    std = global_dict[threading.current_thread().getName()]


# ThreadLocal应运而生，不用查找dict，ThreadLocal帮你自动做这件事：
# 创建全局ThreadLocal对象:
local_school = threading.local


def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

# ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。
