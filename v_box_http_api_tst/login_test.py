# coding:utf8

import cookielib
import urllib2
import urllib
import hashlib
import json
import time

DEBUG = 1

comdic = {"comid":"1","compvtkey":"27a010966282423fbd202bf3f45267c0","isremeber":1}
#comdic = {"comid":"1","compvtkey":"27a010966282423fbd202bf3f45267c0"}
keyval="key=f1cd9351930d4e589922edbcf3b09a7c"
postdate = {"alias":"test_fan","password":"123456","isremeber":1}

# 当前时间戳
nowtime = lambda : int(round(time.time()*1000))

# md5计算
def cal_md5(string):
    p = hashlib.md5()
    p.update(string)
    return p.hexdigest()

# 字典排序和组装
def sign_value(srcdic):
    # 对字典 的 键值 进行 升序排序
    new_dic = sorted(srcdic.iteritems(),key=lambda x:x[0],reverse=False)
    print "new_dict:\n    ", new_dic
    s = ""
    for k,v in new_dic:
        s += "%s=%s&"%(k,v)
    srcsign = s + keyval
    md5value = cal_md5(srcsign)

    if DEBUG:
        print "srcsign\n    ", srcsign
        print "md5value\n    ", md5value

    return md5value

# login mian
urlbase = "http://api.v-box.net/box-data/api/"
urlb = "we-data/login"
url = urlbase+urlb


def get_box(sid):
    ss=("comid=%s&compvtkey=%s&sid=%s&ts=%ls&%s"%(comdic.get("comid"),comdic.get("compvtkey"),sid,comdic.get("ts"),keyval))
    print ss
    newssi = cal_md5(ss)
    print newssi
    nnew = "{"+"\""+"comid"+"\":\"1\"," +"\""+"compvtkey"+"\":\"27a010966282423fbd202bf3f45267c0\"," +"\""+"sid"+"\":\"%s\""%(sid)+",\""+"ts"+"\":%ld,"%(comdic.get('ts'))+"\""+"sign"+"\":\"%s\""%(newssi)+"}"

    print nnew

    urlc = "we-data/boxs"
    url2 = urlbase+urlc

    reqq = urllib2.Request(url2)
    reqq.add_header("common",nnew)
    reqq.add_header("Content-Type",'application/x-www-form-urlencoded')
    reqq.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36')
    reqq.add_header("connection","Keep-Alive")
    reqq.add_header("Host", "192.168.45.186:8686")
    # if DEBUG:
    #     print 'headers: '
    #     print reqq.header_items()
        # print reqq.data
    req = urllib2.urlopen(reqq)    # 发起post
    # if DEBUG:
    #     print req.read()
    #     print req.info()

def run_login():

    # 把password进行md5计算
    newpasw=postdate.get('password')
    postdate['password']=cal_md5(newpasw)
    # body_value = json.dumps(postdate)
    body_value = urllib.urlencode(postdate)
    if DEBUG:
        print "body_value\n    ", body_value

    # 把时间给ts
    comdic['ts']=nowtime()
    # 组合新字典
    dicmerge = dict(postdate,**comdic)
    #if DEBUG:
    #    print dicmerge
    # 排序计算md5
    signmd5 = sign_value(dicmerge)
    comdic['sign'] = signmd5
    #ss = ''
    # 组合sign
    #ss=("alias=%s&comid=%s&compvtkey=%s&isremeber=%d&password=%s&ts=%ls&%s"%(postdate.get('alias'),comdic.get("comid"),comdic.get("compvtkey"),postdate.get('isremeber'),postdate.get("password"),comdic.get("ts"),keyval))
    #print ss
    #comdic['sign'] = cal_md5(ss)
    # 组装comm
    nnew = "{"+"\""+"comid"+"\":\"1\"," +"\""+"compvtkey"+"\":\"27a010966282423fbd202bf3f45267c0\"," +"\""+"ts"+"\":%ld,"%(comdic.get('ts'))+"\""+"sign"+"\":\"%s\""%(comdic.get('sign'))+"}"

    if DEBUG:
        print "comdic\n    ", comdic
        print "nnew\n    ", nnew
        print "bodyvalue\n    ", body_value
    reqq = urllib2.Request(url,data=body_value)
    reqq.add_header("common",nnew)
    reqq.add_header("Content-Type",'application/x-www-form-urlencoded')
    reqq.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36')
    reqq.add_header("connection","Keep-Alive")
    reqq.add_header("Host", "192.168.45.186:8686")
    if DEBUG:
        print "reqq.header_items()\n    ", reqq.header_items()
        print "reqq.data\n    ", reqq.data
    req = urllib2.urlopen(reqq)    # 发起post
    p = req.read()
    if DEBUG:
        print "p\n    ", p
        print "req.info()\n    ", req.info()
    ress = json.loads(p)
    sid = ress.get("result").get('sid')
    print sid
    get_box(sid)


if __name__ == "__main__":
    run_login()