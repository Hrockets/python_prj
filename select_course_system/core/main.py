#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: he zhiyuan

import os,sys,shelve
from conf import settings
from modules.school import School


class Manager_Center(object):

    def __init__(self):
        pass

    def run(self):
        while True:
            print("\n欢迎进入选课系统\n"
                  "1 学生视图\n"
                  "2 讲师视图\n"
                  "3 管理视图\n"
                  "q 退出系统\n")
            user_choice = input('\033[31:1m 请输入你选择的视图>>\033[0m').strip()
            if user_choice == '1':
                Manager_Student()
            elif user_choice == '2':
                Manager_Teacher()
            elif user_choice == '3':
                Manager_School()
            elif user_choice == 'q':
                print('\033[32:1m 欢迎下次使用学员管理系统!\033[0m')
                break
            else:
                print('\033[32:1m please input true choice!\033[0m')

class Manager_Student(object):
    '''
    学生视图
    '''
    def __init__(self):
        if os.path.exists(settings.school_db_file + '.dat'):  # shelve会生成三个文件，其中有.dat结尾
            self.school_db = shelve.open(settings.school_db_file)  # 打开学校数据库文件
            self.run_manage()  # 运行管理视图
            self.school_db.close()  # 关闭数据库文件
        else:
            print('\033[33:1m 系统信息：数据库文件不存在，请先创建学校\033[0m')
            exit()

    def run_manage(self):
        while True:
            print('欢迎来到学生中心\n'
                  '学生注册 student_register\n'
                  '查看学生 check_student\n'
                  '退出程序 exit')
            user_func = input('\033[31:1m 输入要操作的命令>>\033[0m').strip()
            if hasattr(self, user_func):
                func = getattr(self, user_func)
                func()
            else:
                print('\033[32:1m please input true choice!\033[0m')

    def student_register(self):
        for key in self.school_db:
            print('学校名称：', key)  # 打印学校
        choice_school = input('\033[31:1m 输入选择注册的学校名>>\033[0m').strip()
        if choice_school in self.school_db:
            self.choice_school = choice_school
            self.school_obj = self.school_db[choice_school]
            student_name = input('\033[31:1m 输入学生的姓名>>\033[0m').strip()
            student_age = input('\033[31:1m 输入学生的年龄>>\033[0m').strip()
            self.school_obj.show_class_course()
            class_choice = input('\033[31:1m 输入上课的班级>>\033[0m').strip()
            if class_choice in self.school_obj.school_class:
                self.school_obj.create_student(student_name,student_age,class_choice)
                self.school_db.update({self.choice_school: self.school_obj})  # 更新数据库数据
                print('\033[32:1m 学生注册成功\033[0m')
            else:
                print('\033[32:1m 班级不存在\033[0m')
        else:
            print('\033[32:1m 学校不存在\033[0m')

    def check_student(self):
        for key in self.school_db:
            print('学校名称：', key)  # 打印学校
        choice_school = input('\033[31:1m 输入选择注册的学校名>>\033[0m').strip()
        school_obj = self.school_db[choice_school]

        student_name = input('\033[31:1m 输入学生的姓名>>\033[0m').strip()
        flag = 0
        for i in school_obj.school_class:
            class_obj = school_obj.school_class[i]
            if student_name in class_obj.class_student:
                student_obj = class_obj.class_student[student_name]
                print('\033[34:1m 姓名：%s\t 年龄：%s\t 班级：%s\t 关联课程：%s\033[0m' % (student_obj.student_name,
                                                                             student_obj.student_age,
                                                                             class_obj.class_name,
                                                                             class_obj.class_course.course_name))
                flag = 1
        if flag == 0:
            print('\033[32:1m 学生不存在\033[0m')

    def exit(self,*args):
        self.school_db.close()
        sys.exit("\033[32:1m 欢迎下次使用学员管理系统\033[0m")

class Manager_Teacher(object):
    """
    老师视图
    """
    def __init__(self):
        if os.path.exists(settings.school_db_file + '.dat'):  # shelve会生成三个文件，其中有.dat结尾
            self.school_db = shelve.open(settings.school_db_file)  # 打开学校数据库文件
            self.run_manage()  # 运行管理视图
            self.school_db.close()  # 关闭数据库文件
        else:
            print('\033[33:1m 系统信息：数据库文件不存在，请先创建学校\033[0m')
            exit()

    def run_manage(self):
        for key in self.school_db:
            print('学校名称：', key)  # 打印学校
        choice_school = input('\033[31:1m 输入选择的学校名>>\033[0m')
        if choice_school in self.school_db:
            self.choice_school = choice_school
            self.school_obj = self.school_db[choice_school]
            teacher_name = input('\033[31:1m 输入登录讲师的姓名>>\033[0m').strip()
            while True:
                if teacher_name in self.school_obj.school_teacher:
                    print('欢迎来到教师中心\n'
                          '查看班级 check_class\n'
                          '退出程序 exit')
                    user_func = input('\033[31:1m 输入要操作的命令>>\033[0m')
                    if hasattr(self, user_func):
                        func = getattr(self, user_func)
                        func(teacher_name)
                    else:
                        print('\033[32:1m please input true choice!\033[0m')
                else:
                    print('\033[32:1m 讲师不存在\033[0m')

    def check_class(self,teacher_name):
        self.school_obj.show_teacher_classinfo(teacher_name)

    def exit(self,*args):
        self.school_db.close()
        sys.exit("\033[32:1m 欢迎下次使用学员管理系统\033[0m")

class Manager_School(object):
    """
    学校视图
    """
    def __init__(self):
        if os.path.exists(settings.school_db_file + '.dat'):#shelve会生成三个文件，其中有.dat结尾
            self.school_db = shelve.open(settings.school_db_file)#打开学校数据库文件
            self.run_manage()     #运行管理视图
            self.school_db.close()#关闭数据库文件
        else:
            print('\033[33:1m 系统信息：初始化数据库\033[0m')
            self.initialize_school()# 初始化数据库
            self.run_manage()       # 运行管理视图
            self.school_db.close()  # 关闭数据库文件

    def initialize_school(self):
        self.school_db = shelve.open(settings.school_db_file)  # 打开学校数据库文件
        self.school_db['北京'] = School('北京', '中国.北京')
        self.school_db['上海'] = School('上海', '中国.上海')

    def run_manage(self):
        '''运行学校视图'''
        while True:
            for key in self.school_db:
                print('学校名称：',key) #打印学校
            choice_school = input('\033[31:1m 输入选择管理的学校名>>\033[0m')
            if choice_school in self.school_db:
                self.choice_school = choice_school
                self.school_obj = self.school_db[choice_school]
                while True:
                    print('欢迎来到oldboy%s校区\n'
                          '添加课程 add_course\n'
                          '增加班级 add_class\n'
                          '录用讲师 add_teacher\n'
                          '查看课程 check_course\n'
                          '查看班级 check_class\n'
                          '查看老师 check_teacher\n'
                          '退出程序 exit\n' % self.school_obj.school_name)
                    user_func = input('\033[31:1m 输入要操作的命令>>\033[0m')
                    if hasattr(self,user_func):
                        func = getattr(self,user_func)
                        func()
                    else:
                        print('\033[32:1m please input true choice!\033[0m')
            else:
                print('\033[32:1m please input true school choice!\033[0m')

    def add_course(self):
        '''添加课程'''
        course_name = input('\033[34:1m 输入要添加的课程>>\033[0m').strip()
        course_price = input('\033[34:1m 输入要添加的课程价格>>\033[0m').strip()
        course_time = input('\033[34:1m 输入要添加的课程周期>>\033[0m').strip()
        if course_name in self.school_obj.school_course:
            print("\033[34:1m 课程存在\033[0m")
            self.school_obj.create_course(course_name, course_price, course_time)
            print("\033[34:1m 课程更新完成\033[0m")
        else:
            self.school_obj.create_course(course_name, course_price, course_time)
            print("\033[34:1m 课程添加完成\033[0m")

        self.school_db.update({self.choice_school:self.school_obj})# 更新数据库数据

    def add_class(self):
        '''增加班级'''
        class_name = input('\033[34:1m 输入要增加的班级>>\033[0m').strip()
        course_name = input('\033[34:1m 输入要关联的课程>>\033[0m').strip()
        if class_name not in self.school_obj.school_class:
            if course_name in self.school_obj.school_course:
                course_obj = self.school_obj.school_course[course_name]
                self.school_obj.create_class(class_name,course_obj)
                self.school_db.update({self.choice_school:self.school_obj})# 更新数据库数据
            else:
                print("\033[34:1m 系统错误：关联课程不存在\033[0m")
        else:
            print("\033[34:1m 系统错误：班级已经存在\033[0m")

    def add_teacher(self):
        '''录用讲师'''
        teacher_name = input('\033[34:1m 输入要录用讲师的姓名>>\033[0m').strip()
        teacher_salary = input('\033[34:1m 输入要录用讲师的薪水>>\033[0m').strip()
        teacher_class = input('\033[34:1m 输入要录用讲师的关联班级>>\033[0m').strip()
        if teacher_class in self.school_obj.school_class:
            class_obj = self.school_obj.school_class[teacher_class]
            if teacher_name not in self.school_obj.school_teacher:
                self.school_obj.create_teacher(teacher_name,teacher_salary,teacher_class,class_obj)
                print("\033[34:1m 新讲师录用成功\033[0m")
            else:
                self.school_obj.update_teacher(teacher_name,teacher_class,class_obj)
                print("\033[34:1m 讲师已经存在，信息更新完成\033[0m")

            self.school_db.update({self.choice_school: self.school_obj})  # 更新数据库数据
        else:
            print("\033[34:1m 系统错误：关联班级不存在\033[0m")

    def check_course(self):
        self.school_obj.show_course()

    def check_class(self):
        self.school_obj.show_class()

    def check_teacher(self):
        self.school_obj.show_teacher()

    def exit(self):
        self.school_db.close()
        sys.exit("\033[32:1m 欢迎下次使用学员管理系统\033[0m")

