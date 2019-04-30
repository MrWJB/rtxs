#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __str__

class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object ( name: %s )' % self.name

    __repr__ = __str__


s = Student('zhangsan')
print(s)


# __iter__
# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，
# Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a


for n in Fib():
    print(n)

# __getitem__
# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：
'''
>>> Fib()[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'Fib' object does not support indexing
'''


# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
class Fib2():
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

    def __getitem__(self, item):
        a, b = 1, 1
        for x in range(item):
            a, b = b, a + b
        return a


f2 = Fib2()
print(f2[20])


#  __getitem__ 切片的使用

class Fib3():
    def __getitem__(self, item):
        if isinstance(item, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(item, slice):  # n 是切片
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


f3 = Fib3()
print(f3[0:8])


# __getattr__
# 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。比如定义Student类：
class Student3(object):
    def __getattr__(self, attr):
        if attr == 'score':
            return 99


# __call__ 方法
# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。能不能直接在实例本身上调用呢？在Python中，答案是肯定的。
# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。请看示例：

class Student4(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)


# self参数不要传入
s4 = Student4('Michael')
print(s4())

# 能被调用的对象就是一个Callable对象
# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
print(callable(Student4('zhangsan')))

print(callable(max))
