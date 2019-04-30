# -*- coding: utf-8 -*-

from collections import Iterable
import os


# b = isinstance('abc', Iterable)
# print(b)
#
#
# for i, value in enumerate(['A','B','C','D']):
#     print(i,value)
#
#
#
# for x, y in [(1,1),(2,4),(3,9)]:
#     print(x, y)


# v = [x * x for x in range(1, 11) if x % 2 == 0]
# print(v)
#
#
#
# px = [m + n for m in 'ABC' for n in 'CDE']
# print(px)


# dir = [d for d in os.listdir('.')]
# print(dir)


# d = {'x': 'A', 'y': 'B', 'z': 'C' }
# for k, v in d.items():
#     print(k,  '=',  v)


# L = ['Hello', 'World', 'IBM', 'Apple']
# s = [s.lower() for s in L]
# print(s)


# g = (x * x for x in range(1, 11))
# # print(next(g))
# for n in g:
#     print(n)


# 斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


result = fib(20)
print(result)
