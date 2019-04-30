#!/usr/bin/env python3
# -*- coding: utf-8 -*-

i1 = int('12306')
print('i1的值: %s ' % i1)


def int2(x, base=2):
    return int(x, base)


i2 = int2('1010010111011')
print('i2的值: %s' % i2)

# functools.partial 就是帮助我们创建一个偏函数的，不需要我们自己定义int2(), 可以直接使用下面的的代码创建一个新的函数int2：
import functools

int2 = functools.partial(int, base=2)
i3 = int2('1001010101')
print('i3的值: %s' % i3)

# 其它示例
max2 = functools.partial(max, 10)
args = (10, 20, 30, 40, 50)
print(*args)
max3 = max2(*args)
print(max3)
