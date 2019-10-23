#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: he zhiyuan

class Course(object):
    """
    课程类 名称 价格 周期
    """
    def __init__(self,course_name,course_price,course_time):
        self.course_name = course_name
        self.course_price = course_price
        self.course_time = course_time

courses = {'math':'123','phy':'xyz'}
# for key in courses:
#     print(key)
# name = 'math'
# if name in courses:
#     print(1)