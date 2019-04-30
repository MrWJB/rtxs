# -*- coding: utf-8 -*-

import math


# def move(x, y, step,angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny
#
#
# x, y = move(100, 100, 60, math.pi / 6)
# print(x, y)
#
#
# def enroll(name, gender, age=26, city='BeiJing'):
#     print(name)
#     print(gender)
#     print(age)
#     print(city)
#
#
# print(enroll('zhangsan','女'))
#
#
#
# def add_end(L=[]):
#     L.append('END')
#     return L
#
#
# a = add_end([1,2,3])
#
# print(a)


# print(add_end())


# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('end')
#     return L
#
#
# print(add_end())


# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


calc(1, 2)


# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other', kw)


p = person('zhangsan', 22, gender='女')

print(p)

extra = {'city': 'Beijing', 'job': 'Engineer', 'names': 'liuqiang'}
p1 = person('Jack', 24, city=extra['city'], job=extra['job'])
print(p1)

p2 = person('make', 36, **extra)
print(p2)


# 命名关键字参数
def person2(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name', name, 'age', age, 'other', kw)


p3 = person2('zhangsan', 22, city='Beijing', addr='Chaoyang', zipcode=123456)
print(p3)

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

for value in d.values():
    print(value)
