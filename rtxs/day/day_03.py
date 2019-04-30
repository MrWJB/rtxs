#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    f = open('D:/hello.txt', 'r', encoding='gbk', errors='ignore')
    print(f.read())
finally:
    if f:
        f.close()

# with open('D:/hello.txt','r', encoding='gbk') as f:
#     print(f.read())
#
#
# for line in f.readlines():
#     print(line.strip())


with open('D:/hello.txt', 'w', encoding='utf-8') as f:
    f.write('monkey name is gogo')

from io import StringIO

f = StringIO()
print(f)

f.write('hello')
