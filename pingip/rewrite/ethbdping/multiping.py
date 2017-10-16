#!/usr/bin/python
# _*_ coding:utf-8 _*_
# -----------------------------------------------------------
# File Name：     ethbdping_subporcess_single.py
# Description :
#   Author:      fan
#   date:        2017/10/11
#   IDE:         PyCharm Community Edition
# -----------------------------------------------------------

import subprocess
import os, platform
import time, datetime
import threading
import thread
import codecs

global IP_ADDRESSES, QUIT_FLAG
IP_ADDRESSES = []
QUIT_FLAG = False
nowtime = datetime.datetime.now

def get_os():
    """
    get os 类型
    函数返回元组, (pack_lengh, ping_times, '-t'_used, record_coding, how_to_record )
    """
    currentos = platform.system()
    if currentos == 'Windows':
        return 'l', 'n', 't', 'gbk', 3, -2
    else:
        return 's', 'c', ' ', 'utf-8', 5, None


def find_ips(ip_prefix, ip_strt, ip_end):
    """
    给出当前的网段范围，然后扫描整个段所有地址
    """

    def scan_ip(ip_str):
        """
        判断是否ping通，是则加入地址列表
        """
        cmd = ["ping", "-{}".format(get_os()[0]), "8", '-{}'.format(get_os()[1]), '2', ip_str]
        open_ping = os.popen(" ".join(cmd))
        output = open_ping.readlines()

        time.sleep(.1)
        for line in list(output):
            if not line:
                continue
            if str(line).upper().find("TTL") >= 0:
                IP_ADDRESSES.append(ip_str)
                print 'find {}'.format(ip_str)
                break
        # open_ping.close()

    for i in xrange(int(ip_strt), int(ip_end)):
        ip = ip_prefix + '.{}'.format(i)
        thread.start_new_thread(scan_ip, (ip,))
        time.sleep(0.1)


def monitor(ipstr, record_oncee, save_intervall, thread_during):
    """
    在线程中向每个地址发送ping命令，根据回显信息监控其状态，保存信息到指定文件中
    :param ipstr: 单个ip地址
    :param save_intervall: 记录文件的保存间隔，默认30分钟
    :param thread_during: 线程运行多久后退出，默认24小时
    :return:
    """
    global QUIT_FLAG

    used_strt, used_end = get_os()[4:6]
    # 回显信息中响应时间参数的位置单位秒（字符串split方法生成列表）

    filename = ipstr+'.txt'
    logfile = codecs.open(filename, 'a+', 'utf-8')
    time.sleep(0.1)
    logfile.write('\n'+"""\
------------------------------------------------
start ping {0} at {1}
if one address were reachable, the times of
right response with be record with time couple:
[t<=1, 1<t<=5, 5<t<=10, 10<t<=50, 50<t ]
------------------------------------------------\n""".format(
        ipstr, nowtime().strftime('%Y-%m-%d %H:%M:%S')))
    time.sleep(0.1)
    if platform.system() == 'Windows':
        cmd = ['ping', '-l', '1400', '-t', ipstr]
    else:
        cmd = ['ping', '-s', '1400', ipstr]

    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    currentimestr = ''
    thread_start_time = nowtime()
    counter_0_1 = 0
    counter_1_5 = 0
    counter_5_10 = 0
    counter_10_50 = 0
    counter_50_huge = 0

    while not QUIT_FLAG:
        currentime = nowtime()
        currentimestr = currentime.strftime('%Y-%m-%d %H:%M:%S')
        line = popen.stdout.readline()
        if line:
            reline = line[:-1].decode(get_os()[3]).upper()
            towrite = ''
            if reline.upper().find('PING') >= 0:
                towrite = currentimestr + ' ' + reline[:-1]
            elif reline.upper().find('TTL') >= 0:
                # 获取回显信息，只取响应时间的数值，其他信息略去
                retime = reline.split(' ')[-2][used_strt:used_end]
                retimenum = float(retime)
                if retimenum >= 0:
                    if 0 < retimenum <= 1:
                        counter_0_1 += 1
                    elif 1 < retimenum <= 5:
                        counter_1_5 += 1
                    elif 5 < retimenum <= 10:
                        counter_5_10 += 1
                    elif 10 < retimenum <= 50:
                        counter_10_50 += 1
                    else:
                        counter_50_huge += 1
                    towrite = None
                    counters = [counter_0_1, counter_1_5, counter_5_10, counter_10_50, counter_50_huge]
                    if sum(counters) % record_oncee == 0:
                        towrite = currentimestr[-8:] + ' ' + str(counters)

                # linux 平台下处理方式，见下方注释
                # retime = reline.split(' ')[-2]
                # towrite = currentimestr[-8:] + ' ' + retime[5:]
            elif reline.find(u'无法访问' or u'请求超时' or u'UNREACHABLE') >= 0:
                towrite = currentimestr + ' no response'
            else:
                pass
            if towrite:
                logfile.write(towrite+'\n')
        else:
            continue

        delta = int((currentime - thread_start_time).total_seconds())
        # 线程运行的时间，单位s，seconds取整数

        if delta % save_intervall != 0:
            # 判断是否进行保存
            # 根据最后
            continue
        else:
            if delta >= thread_during:
                # 判断是否退出回显监控循环
                logfile.write(currentime.strftime('%Y-%m-%d %H:%M:%S ') + 'monitor quited')
                logfile.close()
                time.sleep(1)
                QUIT_FLAG = True
            else:
                # 执行保存，即执行一次close操作并重新打开
                logfile.write(currentime.strftime('%Y-%m-%d %H:%M:%S ') + 'data saved\n')
                logfile.close()
                time.sleep(1)
                logfile = codecs.open(filename, 'a', 'utf-8')

    time.sleep(.1)

    popen.kill()
    # 将当前线程杀死
    print (currentimestr + ' thread exited')


def main(ippre='192.168.22', ipstrt='1', ipend='255', recordonce=60*1, saveinterval=60*10, duringtime=60*60*24):
    """
    运行多个网络地址ping监控
    :return: no return
    """
    print 'ping {} from {} to {}\n'.format(ippre, ipstrt, ipend), '---- start searching ----'

    ipend = str(int(ipend)+1)
    find_ips(ippre, ipstrt, ipend)
    # 获取符合条件的所有ip地址
    time.sleep(10)
    print '---- end searching ----', '\n\nfind all ip addresses here:'

    for ip in IP_ADDRESSES:
        print ip

    threads = []
    addrs = IP_ADDRESSES
    if addrs is not None:
        for addr in addrs:
            threads.append(threading.Thread(target=monitor, args=(addr, recordonce, saveinterval, duringtime)))
        starttime = datetime.datetime.now()
        print '\nmulti_pings start at ', starttime.strftime('%Y-%m-%d %H:%M:%S')
        for t in threads:
            t.setDaemon(True)
            t.start()
            time.sleep(2)
        for t in threads:
            t.join()
    endtime = datetime.datetime.now()
    print 'multi_pings end at ', endtime.strftime('%Y-%m-%d %H:%M:%S')

if __name__ == "__main__":

    ip_pre, ip_start, ip_endd = '192.168.22', '1', '35'
    # record_once = 60 * 1
    # save_interval = 60 * 2
    # monitor_during_time = 60 * 10
    record_once = 5
    save_interval = 10
    monitor_during_time = 20

    main(ip_pre, ip_start, ip_endd, record_once, save_interval, monitor_during_time)

