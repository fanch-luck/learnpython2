#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 注意：a.将主函数代码写在给定函数范围内（先将“pass”删除）
#       b.将调试代码写在“if __name__ == "__main__":”之后（先将“pass”删除），调试代码不影响评分

"""
8.编写文本管理程序：
实现功能：
程序启动时，进入主界面，主界面中要有菜单：1，新建，2，修改，3，查询，4，统计，5，退出
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
2，查询功能：包含以下菜单和功能：
    1，查询所有：数据来自data.txt列出的所有条目，输入back返回到查询子菜单
    2，查询个人：输入名称，返回职位信息，输入不存在的名称，返回错误提示，
    输入back，返回到查询子菜单。如，输入yun，返回programer，输入"yy"，返回，
    输入有误
    3，返回，返回到主菜单
3，修改功能：包含以下菜单和功能：
    输入要修改的条目序号，输入新的名称和职位，按下enter，原来条目被修改，
    同时保存到data.txt。输入back，返回到主菜单
    举例：输入3 空格 "hh"空格"pp" 回车，文件里面3序号条目，内容被修改
4，统计功能：
    1，统计总的条数，输出，总条数：x条(数据来自data.txt)
    2，统计各个职位有多少人，如：输出：tester：4， programer：3
    3，统计重名人数，并输出：如没有则输出：0，如有则输出：存在2个重名，
    分别是:1:["zhang","ss"]，3:["zhang","yy"]
    4，按下q返回到主菜单
5，退出：结束程序
"""



#  说明： 1，输入必须为： 名字 空格 职位
#         2，先执行new输入数据
#         3, 程序没有严谨判断输入，只是实现基本操作功能

datafile = "data.txt";

def dicttostring(dinput):
    sinput = "";
    sinput += "{"
    sinput += "\n";
    p = [(k,dinput[k]) for k in sorted(dinput.keys())]
    for i in xrange(0,len(p)):
        sinput+= p[i][0];
        sinput+=":[";
        sinput+="\"" + p[i][1].split(" ")[0] + "\",\"" + p[i][1].split(" ")[1] + "]\"";
        sinput += "\n";
    sinput += "}"
    return sinput

class CFile:
    def __init__(self):
        self.file = open(spath,mode='w+');
    def save(self,sInput):
        self.file.write(sInput);
    def read(self):
        return self.file.readlines();
    def __del__(self):
        self.file.close();

class CNewData:
    def __init__(self,sInput):
        self.cfile = CFile(sInput)
    def insert(self):
        sinput = "";
        dinput = {}
        count = 0;
        while(raw_input("INPUT \"F3\" to quit") != "F3"):
            count +=1;
            strr = raw_input();
            dinput[str(count)] = strr;
            #print dinput
        sinput = dicttostring(dinput)
        self.cfile.save(sinput)
        return dinput

class CSelect:
    def __init__(self,sdata):
        self.sdata = sdata

    def seleceone(self,nameInput):
        listname = [];
        count = 0;
        for key in self.sdata:
            value = self.sdata[key];
            name = value.split(" ")[0];
            work = value.split(" ")[1];
            if(name == nameInput):
                count += 1;
                print str(count) + "," + name + ":" + work

    def menu(self):
        while(1):
            print "1 select all"
            print "2 select ?"
            print "3 back"
            nIndex = raw_input("you choose?")
            while(int(nIndex) < 1 or int(nIndex) > 3):
                print "无法解析的命令"
                nIndex = raw_input("you choose?")
            if(nIndex == "1"):
                for key in self.sdata:
                    print key+"," + self.sdata[key]

            elif(nIndex == "2"):
                sname = raw_input("输入名字:")
                self.seleceone(sname)
            elif(nIndex == "3"):
                break;

class CEdit:
    def __init__(self,sInput):
        self.data = sInput
    def menu(self):
        while(1):
            nIndex = raw_input("输入要修改的条目是:");
            if( not self.data.has_key(nIndex)):
                print "没有该条目";
                continue;
            else:
                newstr = raw_input("输入新的值")
                self.data[nIndex] = newstr;
            print "是否继续?(y or n)";
            sanser = raw_input();
            while(sanser !="y" and sanser != "n"):
                print "无法解析的命令"
                print "是否继续?(y or n)";
                sanser = raw_input()
            if (sanser == "y"):
                continue;
            elif (sanser == "n"):
                return self.data
            
    def output(self):
        return self.data

class CCount:
    def __init__(self,sdata):
        self.sdata = sdata;
    def menu(self):
        while(1):
            print "1,count numbers";
            print "2,count work";
            print "3,count same name";
            print "4,press q to quit"
            sIndex = raw_input();
            if(sIndex == "q"):
                break
            while(int(sIndex) <1 or int(sIndex) > 4):
                print "无法解析的命令"
                sIndex = raw_input("重新选择");
            if (sIndex == "1"):
                print "总条数:"+str(len(self.sdata));
            elif (sIndex == "2"):
                self.countWorker()
            elif (sIndex == "3"):
                self.coutSamename()

    def countWorker(self):
        worklist = []
        for key in self.sdata:
            value = self.sdata[key];
            work = value.split(" ")[1];
            worklist.append(work)
        workset = set(worklist)
        for each in workset:
            print each + " 人数: "+str(worklist.count(each));

    def coutSamename(self):
        namelist = []
        worklist = []
        templist = []
        for key in self.sdata:
            value = self.sdata[key];
            name = value.split(" ")[0];
            worklist.append(value.split(" ")[1])
            namelist.append(name)
        templiist = namelist
        nameset = set(namelist)
        for each in nameset:
            num = namelist.count(each);
            worktemplist = []
            if num > 1:
                while(1):
                    try:
                        iindex = templiist.index(each)
                        worktemplist.append(worklist[iindex]);
                        templiist[iindex] = templiist[iindex]+"down";
                    except:
                        break;
                print "重名:" + each;
                print worktemplist;

class CTextDataManageMain:
    def __init__(self,spath):
        self.data = CFile(spath).read()

    def update(self):
        pass

    def menuSetup(self):
        for i in xrange (0,6):
            if(i == 0):
                print "1 new";
            elif (i== 1):
                print "2 edit"
            elif (i == 3):
                print "3 select"
            elif (i == 4):
                print "4 count"
            elif (i == 5):
                print "5 quit"
def setup():
    pass

if __name__ == "__main__":
    import sys
    #CNewData(datafile).insert();
    p = CTextDataManageMain(datafile)
    sdata = "";
    sdatadict = {};

    while(1):
        p.menuSetup();
        select = raw_input("选择菜单");
        id = int(select)
        if(id < 1 or id > 6):
            continue
        else:
            if(id == 1):
                new = CNewData(datafile)
                sdatadict = new.insert();
            elif(id == 2):
                nedit = CEdit(sdatadict)
                sdatadict = nedit.menu();
                svalue = dicttostring(sdatadict);
                pfile = CFile(datafile)
                pfile.save(svalue);
                pfile.__del__();
            elif(id == 3):
                nselect = CSelect(sdatadict);
                nselect.menu();
            elif(id == 4):
                ncount = CCount(sdatadict);
                ncount.menu();
            elif(id == 5):
                sys.exit(0);

