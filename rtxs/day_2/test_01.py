#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)

sl = isinstance(p, Point)
print(sl)

sd = isinstance(p, tuple)
print(sd)

from collections import deque

qe = deque([1, 2, 3, 4, 5, 6])
qe.append('x')
qe.appendleft('z')

print(qe)

qe.pop()
print(qe)
qe.popleft()
print()

from collections import defaultdict

d = defaultdict(lambda: 'N/A')
print(d)

d['key1'] = 'abc'
d['key2'] = 'def'

print(d['key3'])

from urllib import request

with request.urlopen('http://www.baidu.com') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))

req = request.Request('http://www.douban.com/')
req.add_header('User-Agent',
               'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
