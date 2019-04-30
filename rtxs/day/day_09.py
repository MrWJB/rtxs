#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
from datetime import timedelta

dn = datetime.now()  # 获取当前datetime
print(dn)
print(type(dn))

# 用指定日期时间创建datetime
dt = datetime(2019, 4, 23, 15, 13, 40)
print(dt)

# datatime 转 timestamp
sas = dt.timestamp()
print(sas)

cap = datetime.fromtimestamp(dt.timestamp())
print(cap)

# str 转换为datetime
# 首先必须把str转换为datetime，转换方法是通过datetime.strptime()实现，需要一个日期和时间的格式化字符串：
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

# datetime转换为str
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))

# 使用timedelta你可以很容易地算出前几天和后几天的时刻。
now = datetime.now()
print(now)
now = now + timedelta(days=1, hours=12)
print(now)

# 本地时间转换为UTC时间
from datetime import datetime, timedelta, timezone

tz_utc_8 = timezone(timedelta(hours=8))
print(tz_utc_8)
now = datetime.now()
print(now)
