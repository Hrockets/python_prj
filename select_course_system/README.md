# python_prj——select_course_system
'''
实现学校管理课程、班级、教师
学生注册学校课程、查询学生具体信息
教师查询授课情况
'''
select_course_system
----bin
	---__init__.py
	---start.py    #程序入口+添加环境变量查找路径
----conf
	---__init__.py
	---settings.py #数据库路径配置 使用shelve模块
----core
	---__init__.py
	---main.py     #主程序
		---Manager_Center  #主菜单类
		---Manager_Student #学生管理类
		---Manager_Teacher #讲师管理类
		---Manager_School  #学校管理类
----database #使用shelve模块生成的存储文件
----modules
	---__init__.py
	---classs.py #班级类
	---course.py #课程类
	---school.py #学校类
	---student.py#学生类
	---teacher.py#教师类
__init__.py