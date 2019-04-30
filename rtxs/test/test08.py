#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):
    pass


s = Student()
s.name = 'Michael'
print(s.name)


def set_age(self, age):
    self.age = age


from types import MethodType

s.set_age = MethodType(set_age, s)
s.set_age(29)

print(s.age)


# 定义一个类只允许对Dog实例添加name和age属性
# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class Dog(object):
    __slots__ = ('name', 'age')


class Cat(object):
    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
