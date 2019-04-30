#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys

print(len(sys.path))
print(sys.path)


# class Student(object):
#     pass


# bar=Student()
# bar.name='Bart Simpson'
# print(bar.name)


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score


bart = Student('Bart Simpson', 59)
print(bart.name)


def print_score(std):
    print('%s: %s' % (std.name, std.score))


print_score(bart)
