#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Base64是一种用64个字符来表示任意二进制数据的方法。

import base64

res = base64.b64encode(b'binary\x00string')
print(res)

enc = base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
print(enc)

wos = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(wos)

sos = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(sos)

soa = base64.urlsafe_b64decode('abcd--__')
print(soa)
