#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from msilib.schema import Property


class Student(object):
    @Property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @Property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @Property
    def age(self):
        return 2015 - self._birth
