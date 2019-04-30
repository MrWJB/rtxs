#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 判断对象类型，使用type()函数
sf = type(123)
print(sf)

# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
import types


def fun():
    pass


if type(fun) == types.FunctionType:
    print('fn 是函数！')


# 使用isinstance()
# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
class Animal(object):
    pass


class Dog(Animal):
    pass


class Cat(Animal):
    pass


a = Animal()
d = Dog()
c = Cat()

res = isinstance(d, Animal)
print(res)

# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
mes = dir('ABC')
print(mes)


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()
# 获取属性的值
result = hasattr(obj, 'x')
print(result)
# 设置一个属性'y'
sal = setattr(obj, 'y', 19)
print(sal)
# 存在属性'y'
ysl = hasattr(obj, 'y')
print(ysl)
# 获取属性'y'
sals = getattr(obj, 'y')
print(sals)
