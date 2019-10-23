#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: he zhiyuan

class Teacher(object):
    """
    讲师类 姓名 薪水 教授班级
    """
    def __init__(self,teacher_name,teacher_salary):
        self.teacher_name = teacher_name
        self.teacher_salary = teacher_salary
        self.teacher_class = {}  #[14,15]

    def teacher_add_class(self,class_name,class_obj):
        self.teacher_class[class_name] = class_obj
