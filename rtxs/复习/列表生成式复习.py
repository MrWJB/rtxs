#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
# 列表生成式则可以用一行语句代替循环生成上面的list：

rs = [x * x for x in range(1, 11)]
print(rs)

# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
rs2 = [x * x for x in range(1, 11) if x % 2 == 0]
print(rs2)

# 还可以使用两层循环，可以生成全排列：
rs3 = [m + n + x for m in 'ABC' for n in '123' for x in '!@#']
print(rs3)

# 运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
import os

lsdir = [d for d in os.listdir('.')]
print(lsdir)

# 最后把一个list中所有的字符串变成小写：
L = ['Hello', 'World', 'IBM', 'Apple']
ls = [s.lower() for s in L]
print(ls)
