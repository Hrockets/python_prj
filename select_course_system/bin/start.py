#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: he zhiyuan

import os,sys

"""
添加环境变量查找路径
"""
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#sys.path.append(BASE_DIR)
sys.path.insert(0,BASE_DIR)

from core import main

if __name__ == '__main__':
    obj = main.Manager_Center()
    obj.run()

#print(sys.path)
#print(os.path.dirname(__file__))
#print(os.path.abspath(__file__))
#print(BASE_DIR)