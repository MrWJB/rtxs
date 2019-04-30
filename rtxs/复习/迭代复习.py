#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。
# 因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。
# 遍历字典
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

# 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()。
# 迭代value
for value in d.values():
    print(value)

# 迭代key, value
for k, v in d.items():
    print('key: %s , value: %s ' % (k, v))

# 迭代字符串
for str in 'ABC':
    print(str)

# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
from collections import Iterable

vs = isinstance('ABC', Iterable)
print(vs)

sd = isinstance([1, 2, 3], Iterable)
print(sd)

ins = isinstance(123, Iterable)  # 整数是否可迭代
print(ins)

# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
enums = enumerate([1, 2, 3, 4, 5])
print(enums)
for k, v in enumerate([1, 2, 3, 4, 5]):
    print('k: %s , v: %s' % (k, v))

# 上面的for循环里，同时引用了两个变量，在Python里是很常见的，比如下面的代码：
for x, y in [(1, 1), (2, 4), (3, 6), (4, 8)]:
    print(x, y)
