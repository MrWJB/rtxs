#!/usr/bin/env python3
# -*- coding: utf-8 -*-


d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在
# 方法一：
sl = 'Toristor' in d
print(sl)

# 方法二： 二是通过dict提供的get()方法
sl2 = d.get('Toristor')
print(sl2)

# 要删除一个key，用pop(key)方法
sl3 = d.pop('Michael')
print(sl3)

# 请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。

# 和list比较，dict有以下几个特点：
# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。

# 而list相反：
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。

# dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
