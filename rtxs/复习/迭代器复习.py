#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Iterable

# 集合
its = isinstance([], Iterable)
print(its)

# 字典
its2 = isinstance({}, Iterable)
print(its2)

# 字符串
its3 = isinstance('ABC', Iterable)
print(its3)

# 生成式
is4 = isinstance((x for x in range(10)), Iterable)
print(is4)

is5 = isinstance(100, Iterable)
print(is5)

from collections import Iterator

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：

is6 = isinstance(iter([]), Iterator)
print(is6)
# is6 比较 is6_1
is6_1 = isinstance([], Iterator)
print(is6_1)
