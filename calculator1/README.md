# python_prj——calculator

__init__.py
test.py  #用做测试思路实现细节
main.py  #主程序
	operator_update(formula)          #去除空字符，更新运算符处理
	calc_muldiv(formula_list)         #计算乘除
	calc_plumin(operators,num_list)   #计算加减
	merge(plus_minus_operator,multiply_divide_list) 把 * /结尾的合并 2* 3/
	start_calc(formula)               #对括号内部的计算以及无括号的汇总计算
	calculate(formula)                #计算程序主入口, 主要逻辑是先计算括号里的值,算出来后再算乘除,再算加减
