#!/usr/bin/env python3
# -*- coding: utf-8 -*-

List = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print('集合的长度 %s ' % len(List))
print('获取集合的第一个元素 %s ' % List[0])
print('获取集合的最后一个元素 %s ' % List[-1])

print('向集合中添加元素：%s ' % List.append('Marry'))
print('获取集合元素 %s ' % List)

List2 = ['Michael', 'Sarah', ['Tracy', 'Tom'], 'Bob', 'Jack']
print('获取集合中的另一个集合中的tom信息： %s ' % List2[2][1])
