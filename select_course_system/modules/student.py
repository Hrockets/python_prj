#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: he zhiyuan

class Student(object):
    """
    学生类 姓名 年龄
    """
    def __init__(self,student_name,student_age):
        self.student_name = student_name
        self.student_age = student_age