#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from io import StringIO

f = StringIO()
f.write('hello world!')

print(f.getvalue())

import json

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
jsr = json.loads(json_str)
print(jsr)
