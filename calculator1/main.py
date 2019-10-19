#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: he zhiyuan

"""
python计算器——利用re模块实现
1. 寻找输入最深层的括号组合，括号开头结尾内部没有括号
2. 先计算最深层的运算组合，先乘除后加减
"""

import re

def operator_update(formula):
    '''
    计算分组 去除空字符，更新运算符处理
    :param formula: 需要处理的分组
    :return: 去除空格，优化+-的分组
    '''
    formula = formula.replace(' ','')
    formula = formula.replace('+-', '-')
    formula = formula.replace('--', '+')
    return formula

def calc_muldiv(formula_list):
    '''
    计算乘除
    :param formula_list: 乘除列表
    :return: 返回值
    '''
    for index,element in enumerate(formula_list):
        if '*' in element or '/' in element:
            operators = re.findall("[*/]", element)
            calc_list = re.split("[*/]", element)
            num = None
            for i,e in enumerate(calc_list):
                if num:
                    if operators[i-1] == '*':
                        num *=(float)(e)
                    elif operators[i-1] == '/':
                        num /= (float)(e)
                else:
                    num = (float)(e)
            formula_list[index] = num
    return formula_list

def calc_plumin(operators,num_list):
    '''
    计算加减
    :param operators: 运算符列表
    :param num_list:数字列表
    :return:运算结果
    '''
    num = None
    for i,e in enumerate(num_list):
        if num:
            if operators[i-1] == '+':
                num += (float)(e)
            elif operators[i-1] == '-':
                num -= (float)(e)
        else:
            num = (float)(e)
    return num




def merge(plus_minus_operator,multiply_divide_list):
    '''
    把 * /结尾的合并 2* 3/
    :param plus_minus_operator:+-符号列表
    :param multiply_divide_list: 乘除分组列表
    :return: 合并之后的符号列表、乘除分组
    '''
    #2*-5 以‘-’分割 符号是- 列表是2*,5 合并 2*-5
    for index,e in enumerate(multiply_divide_list):
        if e.endswith('*') or e.endswith('/'):
            multiply_divide_list[index] = e + plus_minus_operator[index] + multiply_divide_list[index+1]
            del plus_minus_operator[index]
            del multiply_divide_list[index+1]
            return merge(plus_minus_operator,multiply_divide_list)
    return plus_minus_operator,multiply_divide_list

def start_calc(formula):
    '''
    对括号内部的计算以及无括号的汇总计算
    :param formula: 需要计算的分组
    :return: 返回计算分组的值
    '''
    formula = re.sub('[()]','',formula) #去掉计算分组的括号
    formula = operator_update(formula)  #去掉计算分组的空格和+-优化
    plus_minus_operator = re.findall('[+-]',formula) #+-符号列表
    multiply_divide_list = re.split('[+-]',formula)  #+-分割的乘除数字列表
    #-4*50 以‘-’分割 符号是- 列表是‘’,4*50 合并 -4*50
    if multiply_divide_list[0] == '':#说明以‘-’开头
        multiply_divide_list[1] = '-' + multiply_divide_list[1]
        del plus_minus_operator[0]
        del multiply_divide_list[0]
    res = merge(plus_minus_operator,multiply_divide_list)
    plus_minus_operator = res[0]
    multiply_divide_list = res[1]
    plus_minus_list = calc_muldiv(multiply_divide_list)    #计算乘除
    res = calc_plumin(plus_minus_operator, plus_minus_list)#计算加减
    return res


def calculate(formula):
    '''
    计算程序主入口, 主要逻辑是先计算括号里的值,算出来后再算乘除,再算加减
    :param formula: 运算公式
    :return: 运算结果
    '''
    # 除1~9+-*/() 以外都是非法输入
    temp = re.search('[^[1-9+-/*() ]',formula)
    if temp:
        #print(temp)
        print('Invaild input')
    else:
        while True:
            formula_internal = re.search('\([^()]+\)', formula)
            if formula_internal:
                formula_internal = formula_internal.group()
                res = start_calc(formula_internal)
                formula = formula.replace(formula_internal,str(res))
                print("\33[34;1m%s\33[0m" % (formula))
            else:
                res = start_calc(formula)
                print("\33[31;1m结果:%s\33[0m" % (res))
                break
                #exit()

#s = '1-2*((60-30+(-40*5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
#s = "1 - 2 * ( (60-30 +(-9-2- 5-2*-3-5/3-40*4/2-3/5+6*3) * (-9-2-5-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) -(-4*3)/ (16-3*2) )"

if __name__ == '__main__':
    while True:
        s = input('''------ python's calculator(can input (,),+,-,*,/, ,) ------
        \rplease input >>''').strip()
        #print(s)
        if s == 'q':
            break
        else:
            calculate(s)

