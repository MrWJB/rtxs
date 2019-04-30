#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# tuple和list非常类似，但是tuple一旦初始化就不能修改
# 如果可能，能用tuple代替list的就尽量用tuple
classmates = ('Michael', 'Bob', 'Tracy')
print('获取classmates的第一个元素：%s' % classmates[0])

# 如果要定义一个空的元组
t = ()
print(t)

# 定义一个只有一个元素的tuple
# 定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
t2 = (1)
print(t2)

# 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t3 = (1,)
print(t3)

t = ('a', 'b', ['c', 'd'])
print('获取t元组中集合的第二个元素: %s ' % t[2][1])

# 设置t元组中集合的第一个元素
t[2][0] = 'X'
t[2][1] = 'Y'
print('获取修改后的元组数据：%s ' % len(t))
print(t)

# 要创建一个内容也不变的tuple怎么做？那就必须保证tuple的每一个元素本身也不能变
