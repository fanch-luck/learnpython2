#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 注意：a.将代码写在给定函数范围内（先将“pass”删除）
#       b.将调试代码写在“if __name__ == "__main__":”之后（先将“pass”删除），调试代码不影响评分

"""
4.编写函数，创建新目录“/拷贝目标目录”，遍历目录“/实现拷贝”下所有
文件夹、文件，并将所有含.hsc后缀的文件复制到新目录下。处理完成返回True。
"""
import os, shutil


def look_over(f, t):
        for each in os.listdir(f):
            eachpath = os.path.join(f, each)
            if os.path.isfile(eachpath):
                dir_, file_ = os.path.split(eachpath)
                hsc = file_[-3:]
                if hsc == u'hsc':
                    print eachpath
                    shutil.copyfile(eachpath, os.path.join(t, file_))
            if os.path.isdir(eachpath):
                look_over(eachpath, t)


def func():
    from_dir = u'实现拷贝'
    to_dir = u'拷贝目标目录'
    # os.mkdir(to_dir)
    look_over(from_dir, to_dir)


if __name__ == "__main__":
    func()
