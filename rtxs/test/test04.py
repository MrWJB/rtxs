#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'JiBin Wang'

import sys

print(__name__)
print(sys.argv)
print(len(sys.argv))


def test():
    args = sys.argv
    if len(args) == 1:
        print(sys.argv)
        print(__doc__.__doc__)
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Hello, %s!' % args[1])


if __name__ == '__main__':
    test()


# private函数或变量不应该被别人引用
# 代码封装和抽象的方法
# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；
# 类似__xxx__这样的变量是特殊变量
def _private_1(name):
    return 'Hello, %s' % name


def _private_2(name):
    return 'Hi, %s' % name


def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
