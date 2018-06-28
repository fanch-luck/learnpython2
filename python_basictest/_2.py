#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 注意：
# a.将代码写在给定函数范围内（先将“pass”删除）
# b.将调试代码写在“if __name__ == "__main__":”之后（先将“pass”删除），调试代码不影响评分

"""
2.编写函数，用with句式打开“统计字符.txt”文件并读取所有内容，分别统计
其中：”英文字符”、”空格”、”数字”和”其他字符”的个数。将统计结果存
入一个dict并返回。
"""
import json

def func():
    n_letter = 0
    n_space = 0
    n_digit = 0
    n_other = 0
    with open(u'统计字符.txt', 'r') as f:
        txt = f.read().decode('gbk')
    # print txt
    for i in txt:
        if i == chr(32):
            n_space += 1
        elif i in [chr(asc) for asc in xrange(48, 59)]:
            n_digit += 1
        elif i in [chr(asc) for asc in list(xrange(65, 91)) + list(xrange(97, 123))]:
            n_letter += 1
        else:
            n_other += 1
    dic = {r'英文字符': n_letter,
           r'空格': n_space,
           r'数字': n_digit,
           r'其他字符': n_other}
    return dic



if __name__ == "__main__":
    res = func()
    print json.dumps(res, encoding="UTF-8", ensure_ascii=False)
