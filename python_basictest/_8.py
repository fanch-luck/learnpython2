#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 注意：a.将主函数代码写在给定函数范围内（先将“pass”删除）
#       b.将调试代码写在“if __name__ == "__main__":”之后（先将“pass”删除），调试代码不影响评分

"""
8.编写文本管理程序：
实现功能：
程序启动时，进入主界面，主界面中要有菜单：1，新建，2，修改，3，查询，4，统计，5，退出
可以使用命令行方式或者你已掌握的任何UI设计模块
具体功能说明如下：
1，新建功能：
    键盘输入名称和职位，输入1条，按下回车，继续输入下一条，输入完成后按下F3，
    生成如下格式的data.txt，要覆盖写入，完成后返回主菜单
    {
     1:["yun","programer"],
     2:["ye","tester"],
     3:["zhang","tester"],
     4:["xx":"yy"]
    ｝
2，查询功能：
    包含以下菜单和功能：
    1，查询所有：数据来自data.txt列出的所有条目，输入back返回到查询子菜单
    2，查询个人：输入名称，返回职位信息并打印，输入不存在的名称，返回错误提示，
       输入back，返回到查询子菜单。
    如，输入yun，返回programer并打印；输入yy，提示输入有误，重新输入
    3，返回，返回到主菜单
3，修改功能：
    包含以下功能：
    输入要修改的条目序号，输入新的名称和职位，按下enter，原来条目被修改；
    同时保存到data.txt。输入back，返回到主菜单
    举例：输入【“3空格"hh"空格"pp"】（不包含方括号）按下回车，文件里面3序号条目，
    内容被修改为：3:["hh","pp"]
4，统计功能：
    包含以下菜单和功能：
    1，统计总的条数，输出，总条数：x条(数据来自data.txt)
    2，统计各个职位有多少人，如：输出：tester：4， programer：3
    3，统计重名人数，并输出：如没有则输出：0，如有则输出：存在2个重名，
    分别是:1:["zhang","ss"]，3:["zhang","yy"]
    4，按下q返回到主菜单
5，退出：结束程序
"""
import json


def create():
    print '【1.新建】' \
          '输入和职位(空格隔开)按下回车即输入1条记录，可以连续输入多条，输入完成后按下F3:'
    data = {}
    i = 1
    while True:
        s = raw_input()
        if s == '':
            break
        else:
            ss =s.split(' ')
            print ss
            data[i] = ss
            i += 1

    with open('data.txt', 'w') as f:
        f.write(json.dumps(data))
    print '新建完成！\n'


def inquire():
    with open('data.txt', 'r') as f:
        lines = json.loads(f.read())
    names = []
    for key, value in lines.items():
        names.append(value[0])
    while True:
        s = raw_input("""\
        【2.查询】
        1. 查询所有
        2. 查询个人
        3. 返回
        请输入查询序号，按Enter确认:""")
        if s == '':
            continue
        elif s == '1':
            for key, value in lines.items():
                print key, value[0], value[1]

        elif s == '2':
            ss = raw_input('请输入名字：')
            if ss in names:
                for key, value in lines.items():
                    if ss == value[0]:
                        print key, value[0], value[1]
            elif ss == 'back':
                print '正在返回...\n'
                continue
            else:
                print '输入有误，请重新输入。\n'
                continue
        elif s == '3':
            break
        print '查询完成！'

def modify():
    with open('data.txt', 'r') as f:
        lines = json.loads(f.read())
    s = raw_input('【3.修改】'
                  '输入要修改的序号，后面跟着新的名称和职位（分别以空格相隔），按下Enter确认。\n')
    ss = s.split(' ')
    if len(ss) == 3:
        if ss[0] in lines.keys():
            lines[ss[0]] = ss[1:]
            with open('data.txt', 'w') as ff:
                ff.write(json.dumps(lines))
        else:
            print '要修改的条目不存在。\n'
    elif ss[0] == 'back':
        print '正在返回...\n'
    else:
        print '无法识别的命令。\n'


def count():
    with open('data.txt', 'r') as f:
        lines = json.loads(f.read())
    names = {}
    posts = {}
    for key, [name, post] in lines.items():
        if name not in names.keys():
            names[name] = [{key: [name, post]}]
        else:
            names[name].append({key: [name, post]})
        if post not in posts.keys():
            posts[post] = 1
        else:
            posts[post] += 1
    s = raw_input("""\
    【4.统计】
    1. 统计总人数
    2. 统计各岗位人数
    3. 统计重名情况\n
    """)
    if s == '1':
        print '在数据表中，总人数：', len(lines)
    elif s == '2':
        print '岗位人数统计：\n',
        for post, num in posts.items():
            print post, num, '人'
    elif s == '3':
        print '重名情况统计：\n'
        ss = 0
        for key, value in names.items():
            if len(value) >= 2:
                ss += 1
                print key, '重名{}次\n'.format(len(value))
                for v in value:
                    print v
        if ss == 0:
            print '重名0次\n'
    elif s == 'back':
        print '正在返回...\n'
    else:
        print '无法识别的命令。'



def quit_out():
    print '正在退出...'
    quit()


def func():
    while True:
        type_in = raw_input("""\
    \n主功能菜单
    1. 新建
    2. 查询
    3. 修改
    4. 统计
    5. 退出
    请输入功能序号，按Enter选择：\n
        """)
        if type_in == '1':
            create()
        elif type_in == '2':
            inquire()
        elif type_in == '3':
            modify()
        elif type_in == '4':
            count()
        elif type_in == '5':
            quit_out()
        else:
            print "输入有误，请重新输入：\n"
            continue


if __name__ == "__main__":
    func()
