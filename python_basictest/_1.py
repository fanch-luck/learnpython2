#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 注意：a.将代码写在给定函数范围内（先将“pass”删除）
#       b.将调试代码写在“if __name__ == "__main__":”之后（先将“pass”删除），调试代码不影响评分

"""
1.编写函数，从键盘输入若干年份，中间用半角逗号隔开，例如“1990,1991,2000”，
判断每个年份字符串：
(1)如果年份字符串不是数字，捕获异常并将此判断结果记为-1，
(2)如果年份为闰年则结果记为1，
(3)如果年份为平年则结果记为0。
将每个年份字符串的判断结果按顺序存入一个list并返回。
"""


def func(years):
    years = str(raw_input("请输入若干年份，用半角逗号隔开："))
    l_years = years.split(',')
    l_results = [None] * len(l_years)
    for index in xrange(len(l_years)):
        try:
            i = int(l_years[index])
            if ((i % 4 == 0) and (i % 100 != 0)) or (i % 400 == 0):
                result = 1
            else:
                result = 0
        except Exception as e:
            result = -1
            # print e
        l_results[index] = result
    return l_results


if __name__ == "__main__":
    res = func('')
    print res
