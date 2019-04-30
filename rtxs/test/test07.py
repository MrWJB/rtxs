#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import types


def fn():
    print('fn函数 ....')


if type(fn) == types.FunctionType:
    print('fn')

if type(lambda x: x) == types.LambdaType:
    print('lambada')

if True == isinstance([1, 2, 3, 4], (list, tuple)):
    print('true')

d = dir(str)
print(d)


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()

v = hasattr(obj, 'x')
print(v)
