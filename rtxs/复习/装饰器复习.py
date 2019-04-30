#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 定义一个函数
# def now():
#     print('2015-3-25')

# 将一个函数赋给一个变量
# n = now
# print(n())

# 函数对象有一个__name__属性，可以拿到函数的名字
# print(n.__name__)
# print(now.__name__)


# 在代码运行期间动态增加功能的方式，称之为装饰器
import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('2015-3-25')


if __name__ == '__main__':
    now()
    print(now.__name__)
