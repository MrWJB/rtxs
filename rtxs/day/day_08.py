#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re

es = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
print(es)

rea = re.split(r'\s+', 'a b  c')
print(rea)

sc = re.split(r'[\s\,]+', 'a,b, c  d')
print(sc)

ds = re.split(r'[\s\,\;]+', 'a,b;; c  d')
print(ds)

ssc = re.match('^(\d{3})-(\d{3,8})$', '010-234456')
print(ssc)
