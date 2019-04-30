# -*- coding: utf-8 -*-

def count():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())


# 装饰器
# def now():
#     print('2005-3-25')

# f=now
# f()
# print(now.__name__)

# f=now
# print(f.__name__)

# 在代码运行期间动态增加功能的方式，称之为封装器
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('2005-3-25')


print(now())

revl = int('12345', base=8)
print(revl)


def int2(x, base=2):
    return int(x, base)


print(int2('1000000'))

# 使用偏函数
int2 = functools.partial(int, base=2)
print(int2('100101001'))
