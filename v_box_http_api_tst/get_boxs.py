# coding:utf8
# 功能遍历
__author__ = 'admin'

import os
import urllib2
import urllib
import json
import hashlib
import time

DEBUG = 1

# 当前时间戳
nowtime = lambda : int(round(time.time()*1000))

# 常量设置
urlbase = "http://api.v-box.net/box-data/api/"
#urlbase = "http://192.168.45.186:8686/box-data/api/"
comdic = {"comid":"1","compvtkey":"27a010966282423fbd202bf3f45267c0","isremeber":1}
keyval="key=f1cd9351930d4e589922edbcf3b09a7c"

# md5计算
def cal_md5(string):
    p = hashlib.md5()
    p.update(string)
    return p.hexdigest()

# 字典排序和组装
def sign_value(srcdic):
    # 对字典 的 键值 进行 升序排序
    new_dic = sorted(srcdic.iteritems(),key=lambda x:x[0],reverse=False)
    print new_dic
    s = ""
    for k,v in new_dic:
        s += "%s=%s&"%(k,v)
    srcsign = s + keyval
    md5value = cal_md5(srcsign)
    if DEBUG:
        print srcsign
        print md5value
    return md5value

def sorted_dic(dic):
    new_list = sorted(dic.iteritems(),key=lambda x:x[0],reverse=False)
    return dict(new_list)


def post_run(url,data,common):
    newurl = urlbase + url
    reqq = urllib2.Request(newurl,data=data)
    reqq.add_header("common",common)
    reqq.add_header("Content-Type",'application/x-www-form-urlencoded')
    reqq.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36')
    reqq.add_header("connection","Keep-Alive")
    reqq.add_header("Host", "192.168.45.186:8686")
    if DEBUG:
        print reqq.header_items()
        print reqq.data
    req = urllib2.urlopen(reqq)    # 发起post
    return req.read()

# 登录
def login():
    f = open(".\\login.txt","a+")
    url = "we-data/login"

    postdate = {"alias":"779789937@qq.com","password":"123123","isremeber":1}
    # 把password进行md5计算
    newpasw=postdate.get('password')
    postdate['password']=cal_md5(newpasw)
    # body_value = json.dumps(postdate)
    body_value = urllib.urlencode(postdate)

    # 把时间给ts
    comdic['ts']=nowtime()

    # 组合sign
    ss=("alias=%s&comid=%s&compvtkey=%s&isremeber=%d&password=%s&ts=%ls&%s"%(postdate.get('alias'),comdic.get("comid"),comdic.get("compvtkey"),postdate.get('isremeber'),postdate.get("password"),comdic.get("ts"),keyval))
    comdic['sign'] = cal_md5(ss)
    # 组装comm
    nnew = "{"+"\""+"comid"+"\":\"1\"," +"\""+"compvtkey"+"\":\"27a010966282423fbd202bf3f45267c0\"," +"\""+"ts"+"\":%ld,"%(comdic.get('ts'))+"\""+"sign"+"\":\"%s\""%(comdic.get('sign'))+"}"

    if DEBUG:
        print comdic
        print nnew
    # 返回sid
    p = post_run(url,data=body_value,common=nnew)
    f.write(body_value+"\n")
    f.write(p+"\n")
    f.close()
    ress = json.loads(p)
    sid = ress.get("result").get('sid')
    if DEBUG:
        print sid
    return sid

# 获得盒子数据
def get_boxs(sid):
    f = open(".\\boxs.txt","a+")
    url = "we-data/boxs"
    # 把时间给ts
    comdic['ts']=nowtime()
    # 组合sign
    ss=("comid=%s&compvtkey=%s&sid=%s&ts=%ls&%s"%(comdic.get("comid"),comdic.get("compvtkey"),sid,comdic.get("ts"),keyval))
    newssi = cal_md5(ss)
    # 组装comm
    nnew = "{"+"\""+"comid"+"\":\"1\"," +"\""+"compvtkey"+"\":\"27a010966282423fbd202bf3f45267c0\"," +"\""+"sid"+"\":\"%s\""%(sid)+",\""+"ts"+"\":%ld,"%(comdic.get('ts'))+"\""+"sign"+"\":\"%s\""%(newssi)+"}"

    if DEBUG:
        print ss
        print comdic
        print nnew
    # 返回所有的盒子
    p = post_run(url,data=None,common=nnew)
    # 获取boxid
    f.write(p+"\n")
    f.close()
    t = json.loads(p)
    ll = t.get("result").get("list")
    boxidl = []
    for each in ll:
        p = each.get('boxList')
        for eachp in p:
            boxidl.append(eachp.get('boxId'))
    if DEBUG:
        print t
        print ll
        print boxidl
    return boxidl
def get_box_realgroups(sid,boxid):
    f = open(".\\realgroup.txt","a+")
    url = "we-data/realgroups"
    # 数据
    post_date = {"boxId":2}
    post_date["boxId"]=boxid
    body_value = urllib.urlencode(post_date)
    # 把时间给ts
    comdic['ts']=nowtime()
    # 组合sign
    ss=("boxId=%d&comid=%s&compvtkey=%s&sid=%s&ts=%ls&%s"%(boxid,comdic.get("comid"),comdic.get("compvtkey"),sid,comdic.get("ts"),keyval))
    newssi = cal_md5(ss)
    # 组装comm
    nnew = "{"+"\""+"comid"+"\":\"1\"," +"\""+"compvtkey"+"\":\"27a010966282423fbd202bf3f45267c0\"," +"\""+"sid"+"\":\"%s\""%(sid)+",\""+"ts"+"\":%ld,"%(comdic.get('ts'))+"\""+"sign"+"\":\"%s\""%(newssi)+"}"

    if DEBUG:
        print ss
        print comdic
        print nnew
    # 返回所有的盒子
    p = post_run(url,data=body_value,common=nnew)
    f.write(body_value+"\n")
    f.write(p+"\n")
    f.close()
    if DEBUG:
        print p
    t = json.loads(p)
    grouplist = t.get("result").get("list")
    b = []
    for each in grouplist:
        b.append(each.get("groupId"))
    return b
# 3.实时监控点配置列表
def get_box_realgroupcnf(sid,boxid,groupid,pagesize,pageindex):
    f = open(".\\realgroupcnf.txt","a+")
    url = "we-data/realcfgs"
    # 数据
    post_date = {"boxId":2,"groupId":1,"pageIndex":1,"pageSize":1}
    post_date["boxId"]=boxid
    post_date["groupId"] = groupid
    post_date["pageIndex"] = pageindex
    post_date["pageSize"] = pagesize
    body_value = urllib.urlencode(post_date)
    # 把时间给ts
    comdic['ts']=nowtime()
    # 组合sign
    ss=("boxId=%d&comid=%s&compvtkey=%s&groupId=%d&pageIndex=%d&pageSize=%d&sid=%s&ts=%ls&%s"%(boxid,comdic.get("comid"),comdic.get("compvtkey"),groupid,pageindex,pagesize,sid,comdic.get("ts"),keyval))
    newssi = cal_md5(ss)
    # 组装comm
    nnew = "{"+"\""+"comid"+"\":\"1\"," +"\""+"compvtkey"+"\":\"27a010966282423fbd202bf3f45267c0\"," +"\""+"sid"+"\":\"%s\""%(sid)+",\""+"ts"+"\":%ld,"%(comdic.get('ts'))+"\""+"sign"+"\":\"%s\""%(newssi)+"}"

    if DEBUG:
        print ss
        print comdic
        print nnew
    # 返回所有的盒子
    p = post_run(url,data=body_value,common=nnew)
    f.write(body_value+"\n")
    f.write(p+"\n")
    f.close()
    if DEBUG:
        print p
    t = json.loads(p)

# 4.实时监控点数据列表,返回monitorid
def get_box_realdate(sid,boxid,groupid,pagesize,pageindex):
    f = open(".\\realdate.txt","a+")
    url = "we-data/realdata"
    # 数据
    post_date = {"boxId":2,"groupId":1,"pageIndex":1,"pageSize":1}
    post_date["boxId"]=boxid
    post_date["groupId"] = groupid
    post_date["pageIndex"] = pageindex
    post_date["pageSize"] = pagesize
    body_value = urllib.urlencode(post_date)
    # 把时间给ts
    comdic['ts']=nowtime()
    # 组合sign
    ss=("boxId=%d&comid=%s&compvtkey=%s&groupId=%d&pageIndex=%d&pageSize=%d&sid=%s&ts=%ls&%s"%(boxid,comdic.get("comid"),comdic.get("compvtkey"),groupid,pageindex,pagesize,sid,comdic.get("ts"),keyval))
    newssi = cal_md5(ss)
    # 组装comm
    nnew = "{"+"\""+"comid"+"\":\"1\"," +"\""+"compvtkey"+"\":\"27a010966282423fbd202bf3f45267c0\"," +"\""+"sid"+"\":\"%s\""%(sid)+",\""+"ts"+"\":%ld,"%(comdic.get('ts'))+"\""+"sign"+"\":\"%s\""%(newssi)+"}"

    if DEBUG:
        print ss
        print comdic
        print nnew
    # 返回所有的盒子
    p = post_run(url,data=body_value,common=nnew)
    f.write(body_value+"\n")
    f.write(p+"\n")
    f.close()
    if DEBUG:
        print p
    t = json.loads(p)
    listl = t.get("result").get("list")
    monilist = []
    for each in listl:
        monilist.append(each.get("monitorId"))
    if DEBUG:
        print monilist
    return monilist

# 对数据进行更新
def update_real_data(sid,monitorid,value):
    f = open(".\\update.txt","a+")
    url = "we-data/updrealdata"
    post_date = {"monitorId":2,"value":1}
    post_date["monitorId"]=monitorid
    post_date["value"] = value

    body_value = urllib.urlencode(post_date)
    # 把时间给ts
    comdic['ts']=nowtime()
    # 组合sign
    ss=("comid=%s&compvtkey=%s&monitorId=%d&sid=%s&ts=%ls&value=%s&%s"%(comdic.get("comid"),comdic.get("compvtkey"),monitorid,sid,comdic.get("ts"),value,keyval))
    newssi = cal_md5(ss)
    # 组装comm
    nnew = "{"+"\""+"comid"+"\":\"1\"," +"\""+"compvtkey"+"\":\"27a010966282423fbd202bf3f45267c0\"," +"\""+"sid"+"\":\"%s\""%(sid)+",\""+"ts"+"\":%ld,"%(comdic.get('ts'))+"\""+"sign"+"\":\"%s\""%(newssi)+"}"

    if DEBUG:
        print ss
        print comdic
        print nnew
    # 返回所有的盒子
    p = post_run(url,data=body_value,common=nnew)
    f.write(body_value+"\n")
    f.write(p+"\n")
    f.close()
    if DEBUG:
        print p
    t = json.loads(p)

# 获得历史监控点,chage =1 传送boxid,chage !=1 不发送boxid
def get_his_monitor_date(sid,chage,boxid):
    f = open(".\\monitors.txt","a+")
    url = "we-data/monitors"
    post_date = {"boxId":2}
    post_date["boxId"]=boxid
    body_value = urllib.urlencode(post_date)
    # 把时间给ts
    comdic['ts']=nowtime()
    # 组合sign
    if chage == 1:
        ss=("boxId=%d&comid=%s&compvtkey=%s&sid=%s&ts=%ls&%s"%(boxid,comdic.get("comid"),comdic.get("compvtkey"),sid,comdic.get("ts"),keyval))
    else:
        ss=("comid=%s&compvtkey=%s&sid=%s&ts=%ls&%s"%(comdic.get("comid"),comdic.get("compvtkey"),sid,comdic.get("ts"),keyval))
    newssi = cal_md5(ss)
    # 组装comm
    nnew = "{"+"\""+"comid"+"\":\"1\"," +"\""+"compvtkey"+"\":\"27a010966282423fbd202bf3f45267c0\"," +"\""+"sid"+"\":\"%s\""%(sid)+",\""+"ts"+"\":%ld,"%(comdic.get('ts'))+"\""+"sign"+"\":\"%s\""%(newssi)+"}"

    if DEBUG:
        print ss
        print comdic
        print nnew
    # 返回所有的盒子
    if chage == 1:
        p = post_run(url,data=body_value,common=nnew)
        f.write(body_value+"\n")
    else:
        p = post_run(url,data=None,common=nnew)
    f.write(p+"\n")
    f.close()
    if DEBUG:
        print p
    t = json.loads(p)
    tt = t.get("result").get("list")
    hismoni = []
    for each in tt:
        hismoni.append(each.get("monitorId"))
    return hismoni

# 获得历史数据
def get_his_data_list(sid,chage,monitorid,monitorbegin,monitorend,pagesize,pageindex):
    f = open(".\\his_date.txt","a+")
    url = "we-data/historydata"
    post_date = {}
    # 把时间给ts
    comdic['ts']=nowtime()

    post_date["monitorId"] = monitorid
    post_date["pageIndex"] = pageindex
    post_date["pageSize"] = pagesize

    # 组合sign
    if chage == 1:
        body_value = urllib.urlencode(post_date)
        ss=("comid=%s&compvtkey=%s&monitorId=%d&pageIndex=%d&pageSize=%d&sid=%s&ts=%ls&%s"%(comdic.get("comid"),comdic.get("compvtkey"),monitorid,pageindex,pagesize,sid,comdic.get("ts"),keyval))
    elif chage == 2:
        body_value = "monitorBeginTime=%s&monitorId=%d&pageIndex=%d&pageSize=%d"%(monitorbegin,monitorid,pageindex,pagesize)
        ss=("comid=%s&compvtkey=%s&monitorBeginTime=%s&monitorId=%d&pageIndex=%d&pageSize=%d&sid=%s&ts=%ls&%s"%(comdic.get("comid"),comdic.get("compvtkey"),monitorbegin,monitorid,pageindex,pagesize,sid,comdic.get("ts"),keyval))
    elif chage == 3:
        body_value = "monitorEndTime=%s&monitorId=%d&pageIndex=%d&pageSize=%d"%(monitorend,monitorid,pageindex,pagesize)
        ss=("comid=%s&compvtkey=%s&monitorEndTime=%s&monitorId=%d&pageIndex=%d&pageSize=%d&sid=%s&ts=%ls&%s"%(comdic.get("comid"),comdic.get("compvtkey"),monitorend,monitorid,pageindex,pagesize,sid,comdic.get("ts"),keyval))
    elif chage == 4:
        body_value = "monitorBeginTime=%s&monitorEndTime=%s&monitorId=%d&pageIndex=%d&pageSize=%d"%(monitorbegin,monitorend,monitorid,pageindex,pagesize)
        ss=("comid=%s&compvtkey=%s&monitorBeginTime=%s&monitorEndTime=%s&monitorId=%d&pageIndex=%d&pageSize=%d&sid=%s&ts=%ls&%s"%(comdic.get("comid"),comdic.get("compvtkey"),monitorbegin,monitorend,monitorid,pageindex,pagesize,sid,comdic.get("ts"),keyval))

    newssi = cal_md5(ss)
    # 组装comm
    nnew = "{"+"\""+"comid"+"\":\"1\"," +"\""+"compvtkey"+"\":\"27a010966282423fbd202bf3f45267c0\"," +"\""+"sid"+"\":\"%s\""%(sid)+",\""+"ts"+"\":%ld,"%(comdic.get('ts'))+"\""+"sign"+"\":\"%s\""%(newssi)+"}"

    if DEBUG:
        print ss
        print comdic
        print nnew
        print body_value
    # 返回所有的盒子
    p = post_run(url,data=body_value,common=nnew)
    f.write(body_value+"\n")
    f.write(p+"\n")
    f.close()
    if DEBUG:
        print p
    t = json.loads(p)

# 获得报警数据
def get_alarm_data_list(sid,chage,boxid,monitorbegin,monitorend,pagesize,pageindex,state,alarmtype,alarmlevel):
    f = open(".\\alarm.txt","a+")
    url = "we-data/alarmdata"
    post_date = {}
    # 把时间给ts
    comdic['ts']=nowtime()
    ss = ""

    # 组合sign
    if chage == 1:
        body_value = "boxId=%d&pageIndex=%d&pageSize=%d&state=%d"%(boxid,pageindex,pagesize,state)
        ss=("boxId=%d&comid=%s&compvtkey=%s&pageIndex=%d&pageSize=%d&sid=%s&state=%d&ts=%ls&%s"%(boxid,comdic.get("comid"),comdic.get("compvtkey"),pageindex,pagesize,sid,state,comdic.get("ts"),keyval))
    elif chage == 2:
        body_value = "boxId=%d&monitorBeginTime=%s&pageIndex=%d&pageSize=%d&state=%d"%(boxid,monitorbegin,pageindex,pagesize,state)
        ss=("boxId=%d&comid=%s&compvtkey=%s&monitorBeginTime=%s&pageIndex=%d&pageSize=%d&sid=%s&state=%d&ts=%ls&%s"%(boxid,comdic.get("comid"),comdic.get("compvtkey"),monitorbegin,pageindex,pagesize,sid,state,comdic.get("ts"),keyval))
    elif chage == 3:
        body_value = "boxId=%d&monitorEndTime=%s&pageIndex=%d&pageSize=%d&state=%d"%(boxid,monitorend,pageindex,pagesize,state)
        ss=("boxId=%d&comid=%s&compvtkey=%s&monitorEndTime=%s&pageIndex=%d&pageSize=%d&sid=%s&state=%d&ts=%ls&%s"%(boxid,comdic.get("comid"),comdic.get("compvtkey"),monitorend,pageindex,pagesize,sid,state,comdic.get("ts"),keyval))
    elif chage == 4:
        body_value = "boxId=%d&monitorBeginTime=%s&monitorEndTime=%s&pageIndex=%d&pageSize=%d&state=%d"%(boxid,monitorbegin,monitorend,pageindex,pagesize,state)
        ss=("boxId=%d&comid=%s&compvtkey=%s&monitorBeginTime=%s&monitorEndTime=%s&pageIndex=%d&pageSize=%d&sid=%s&state=%d&ts=%ls&%s"%(boxid,comdic.get("comid"),comdic.get("compvtkey"),monitorbegin,monitorend,pageindex,pagesize,sid,state,comdic.get("ts"),keyval))
    elif chage == 5:
        body_value = "alarmType=%d&boxId=%d&pageIndex=%d&pageSize=%d&state=%d"%(alarmtype,boxid,pageindex,pagesize,state)
        ss=("alarmType=%d&boxId=%d&comid=%s&compvtkey=%s&pageIndex=%d&pageSize=%d&sid=%s&state=%d&ts=%ls&%s"%(alarmtype,boxid,comdic.get("comid"),comdic.get("compvtkey"),pageindex,pagesize,sid,state,comdic.get("ts"),keyval))
    elif chage == 6:
        body_value = "alarmLevel=%d&boxId=%d&pageIndex=%d&pageSize=%d&state=%d"%(alarmlevel,boxid,pageindex,pagesize,state)
        ss=("alarmLevel=%d&boxId=%d&comid=%s&compvtkey=%s&pageIndex=%d&pageSize=%d&sid=%s&state=%d&ts=%ls&%s"%(alarmlevel,boxid,comdic.get("comid"),comdic.get("compvtkey"),pageindex,pagesize,sid,state,comdic.get("ts"),keyval))
    elif chage == 7:
        body_value = "alarmLevel=%d&alarmType=%d&boxId=%d&pageIndex=%d&pageSize=%d&state=%d"%(alarmlevel,alarmtype,boxid,pageindex,pagesize,state)
        ss=("alarmLevel=%d&alarmType=%d&boxId=%d&comid=%s&compvtkey=%s&pageIndex=%d&pageSize=%d&sid=%s&state=%d&ts=%ls&%s"%(alarmlevel,alarmtype,boxid,comdic.get("comid"),comdic.get("compvtkey"),pageindex,pagesize,sid,state,comdic.get("ts"),keyval))
    elif chage == 8:
        body_value = "alarmLevel=%d&alarmType=%d&boxId=%d&monitorBeginTime=%s&monitorEndTime=%s&pageIndex=%d&pageSize=%d&state=%d"%(alarmlevel,alarmtype,boxid,monitorbegin,monitorend,pageindex,pagesize,state)
        ss=("alarmLevel=%d&alarmType=%d&boxId=%d&comid=%s&compvtkey=%s&monitorBeginTime=%s&monitorEndTime=%s&pageIndex=%d&pageSize=%d&sid=%s&state=%d&ts=%ls&%s"%(alarmlevel,alarmtype,boxid,comdic.get("comid"),comdic.get("compvtkey"),monitorbegin,monitorend,pageindex,pagesize,sid,state,comdic.get("ts"),keyval))

    # 对字典排序
    # new_post = sorted_dic(post_date)
    # body_value = urllib.urlencode(post_date)
    newssi = cal_md5(ss)
    # 组装comm
    nnew = "{"+"\""+"comid"+"\":\"1\"," +"\""+"compvtkey"+"\":\"27a010966282423fbd202bf3f45267c0\"," +"\""+"sid"+"\":\"%s\""%(sid)+",\""+"ts"+"\":%ld,"%(comdic.get('ts'))+"\""+"sign"+"\":\"%s\""%(newssi)+"}"

    if DEBUG:
        print ss
        print comdic
        print nnew
        print body_value

    p = post_run(url,data=body_value,common=nnew)
    f.write(body_value+"\n")
    f.write(p+"\n")
    f.close()
    if DEBUG:
        print p
    t = json.loads(p)

if __name__=="__main__":
    boxid = 0
    sid = login()
    print '------------------------get_box_id--------------------------\n'
    boxidlist = get_boxs(sid)
    if DEBUG:
        print boxidlist
    for eachbox in boxidlist:
        boxid = int(eachbox)
        # 获得盒子的groupid
        print '------------------------get_group_id------------------------\n'
        p = get_box_realgroups(sid,boxid=boxid)
        if DEBUG:
            print p

        for i in p:
            # 获得具体的配置
            print "--------------get_real_group_config-------------------------\n"
            get_box_realgroupcnf(sid,boxid=boxid,groupid=i,pagesize=100,pageindex=1)
            # 获得监控点数据列表
            print "--------------get_real_date_list-----------------------------\n"
            try:
                monitor = get_box_realdate(sid,boxid=boxid,groupid=i,pagesize=200,pageindex=1)
                for each in monitor:
                    print "-----------------------to_updata_value----------------------------\n"
                    update_real_data(sid,each,"1")
            except Exception,e:
                print "------no monitor data-----\n"
                print "message:"+e.message
                pass

        print "--------------------------get_his_monitor_date--------------------------\n"
        try:
            hismoni = get_his_monitor_date(sid,1,boxid)
            for eachhis in hismoni:
                print "--------------------------get_his_data_list_with_nobegin_noendtime---------------\n"
                get_his_data_list(sid,1,eachhis,monitorbegin=None,monitorend=None,pagesize=10,pageindex=1)
                print "--------------------------get_his_data_list_with_begin---------------------------\n"
                get_his_data_list(sid,2,eachhis,monitorbegin="2018-01-24 13:35",monitorend=None,pagesize=200,pageindex=1)
                print "--------------------------get_his_data_list_with_endtime-------------------------\n"
                get_his_data_list(sid,3,eachhis,monitorbegin=None,monitorend="2018-01-24 13:40",pagesize=200,pageindex=1)
                print "--------------------------get_his_data_list_with_begin_endtime--------------------\n"
                get_his_data_list(sid,4,eachhis,monitorbegin="2018-01-24 13:35",monitorend="2018-01-24 13:40",pagesize=100,pageindex=1)
        except Exception,e:
            print "---------------------no his monitor data-----------------------------\n"
            print "message:"+e.message
            pass

        print "--------------------------get_alarm_date--------------------------\n"
        try:
            for eachs in [1,2]:
                state = eachs
                for eachtype in [0,1]:
                    alarmtype = eachtype
                    for eachle in [1,2,3]:
                        alarmlevel = eachle
                        for chage in xrange(1,9):
                            print "--------------------------get_alarm_data_with_state_%d_alarmtype=%d_alarmlevel=%d_chage=%d---------------\n"%(state,alarmtype,alarmlevel,chage)
                            get_alarm_data_list(sid,chage=chage,boxid=boxid,monitorbegin="2018-01-24 13:35",monitorend="2018-01-24 13:40",pagesize=200,pageindex=1,state=state,alarmtype=alarmtype,alarmlevel=alarmlevel)
        except Exception,e:
            print "---------------------no alarm data-----------------------------\n"
            print "message:"+e.message
            pass


