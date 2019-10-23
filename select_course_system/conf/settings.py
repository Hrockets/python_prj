#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: he zhiyuan

import os,sys
"""
配置数据库的路径
"""
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
database_path = os.path.join(BASE_DIR,"database")

school_db_file = os.path.join(database_path,'school')
#print(BASE_DIR)
#print(database_path)
#print(school_db_file)