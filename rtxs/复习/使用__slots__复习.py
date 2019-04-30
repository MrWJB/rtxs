#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    pass


s = Student()
s.name = 'zhangsna'
print(s.name)


def set_age(self, age):
    self.age = age


from types import MethodType

# 给Student实例绑定方法
s.set_age = MethodType(set_age, s)
# 调用实例方法
s.set_age(22)
# 获取age
print(s.age)


# 但是，给一个实例绑定的方法，对另一个实例是不起作用的：
# 为了给所有实例都绑定方法，可以给class绑定方法：
def set_score(self, score):
    self.score = score


# 为了给所有实例都绑定方法，可以给class绑定方法：
Student.set_score = set_score

s2 = Student()
s2.set_score(280)
print(s2.score)

s.set_score(200)
print(s.score)


# 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：

class Cot(object):
    __slots__ = ('name', 'age')


c = Cot()
c.age = 22
c.name = '奶牛'
# c.price = 222222
print(c)
