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


def generatePlateNumber():
    import random
    platenumber="";
    head = "闽A";
    platenumber+=head;
    while(1):
        # 第一位
        first = random.randint(0,9);
        # 最后一位
        tail = random.randint(0,9);
        second = 0;
        third = 0;
        four = 0;
        # 中间3位
        while(1):
            second = random.randint(0,9)  if random.randint(0,1) else random.randint(65,68);
            third = random.randint(0,9)  if random.randint(0,1) else random.randint(65,68);
            four = random.randint(0,9)  if random.randint(0,1) else random.randint(65,68);
            sums = second + third + four
            if(sums < 86 and sums > 27):
                break
        s = [];
        s.append(first);
        s.append(second);
        s.append(third);
        s.append(four);
        s.append(tail);
        if (s.count(0) < 4):
            break;

    platenumber += str(first)
    platenumber += str(second) if second < 65 else chr(second);
    platenumber += str(third) if third < 65 else chr(third);
    platenumber += str(four) if four < 65 else chr(four);
    platenumber += str(tail)
    return platenumber;

if __name__ == "__main__":
    print generatePlateNumber()
