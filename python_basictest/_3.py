#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 注意：a.将代码写在给定函数范围内（先将“pass”删除）
#       b.将调试代码写在“if __name__ == "__main__":”之后（先将“pass”删除），调试代码不影响评分

"""
3.x1、x2分别是一个二进制数字和16进制数字表示的字符串，编写函数，求它们的十进制整数值。
将结果存入list并返回
"""


def func():
    x1 = '1001011'
    x2 = 'a35bf'
    i_x1 = int('0b' + x1, 2)
    i_x2 = int('0x' + x2, 16)
    return [i_x1, i_x2]

if __name__ == "__main__":
    print func()
