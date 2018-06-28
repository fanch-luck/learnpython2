#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 注意：a.将代码写在给定函数范围内（先将“pass”删除）
#       b.将调试代码写在“if __name__ == "__main__":”之后（先将“pass”删除），调试代码不影响评分

"""
10.编写函数实现一个自选车牌号自动生成程序，车牌号由“闽A”和其他5个字符组成，这5个字符必须满足
以下条件：
   1、第一位和最后一位必须是数字；
   2、第二、三、四位中任意一位且只有一位必须是英文字母，英文字母是A、B、C、D中的一个；
   3、数字不能全部为0
   如：生成的车牌号为“闽A44B08”，将此字符串作为函数的返回值
"""
import random

def func():
    l = []
    choose_digit = lambda: random.choice('1234567890')
    for i in range(5):
        l.append(choose_digit())
    letter_position = int(random.choice('234'))
    letter = random.choice('ABCD')
    l[letter_position-1] = letter
    car_code = "闽A" + ''.join(l)
    if car_code.count('0') == 4:
        return func()
    else:
        return car_code


if __name__ == "__main__":
    print func()
