#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 注意：a.将代码写在给定函数范围内（先将“pass”删除）
#       b.将调试代码写在“if __name__ == "__main__":”之后（先将“pass”删除），调试代码不影响评分

"""
5.公司需要建立职员数据库，表单需录入职员个人信息，其中姓名、性别、岗位
是必填项，工作性质默认为全日制，特长至少一项也可以有多项，个人电话、个
人邮箱等等其他信息为选填项目，请设计一个class实现以下特性：
    1.在初始化时接收这些职员信息，
    2.实现上述信息录入过程的特性
    3.实现通过其方法一次性打印出这些信息。
"""


class Staff(object):
    def __init__(self, name, gender, post, work_nature='full-time', *strong_points, **others):
        self.name = name
        self.gender = gender
        self.post = post
        self.work_nature = work_nature
        self.strong_points = strong_points
        self.other_info = others

        self.prt_info()

    def prt_info(self):
        print """\
    Staff info:
        name: {}
        gender: {}
        post: {}
        work_nature: {}
        strong_points: {}
        """.format(self.name, self.gender, self.post, self.work_nature, self.strong_points)
        print '    othor infos:'
        for key, value in self.other_info.items():
            print '        '+key + ': ' + value


if __name__ == "__main__":
    xiaoming = Staff('xiaoming', 'male', 'manager', 'full-time', 'speek', 'running',
                     phone_number='13188888888', mail='xm@qq.com')
