#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: he zhiyuan

import re


s = '+-*/() 123456789'
s = re.search('[^[1-9+-/*() ]',s)
print(s)
# res = 'abc123'
# d = re.findall(r'[^[1-9]',res)
# print(d)