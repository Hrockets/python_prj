#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: he zhiyuan

class Class(object):
    """
    班级类 名称 课程 学生
    """
    def __init__(self,class_name,course_obj):
        self.class_name = class_name
        self.class_course= course_obj
        self.class_student = {}
