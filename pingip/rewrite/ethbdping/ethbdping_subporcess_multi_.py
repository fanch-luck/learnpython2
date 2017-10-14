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
        return 'l', 'n', 't', 'gbk', 2
    else:
        return 's', 'c', ' ', 'utf-8', 5


def find_ips(ip_prefix='192.168.22'):
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

    for i in xrange(200, 202):
        ip = ip_prefix + '.{}'.format(i)
        thread.start_new_thread(scan_ip, (ip,))
        time.sleep(0.1)


def monitor(ipstr):
    global QUIT_FLAG
    thread_during = 12
    save_interval = 5
    used_piece = get_os()[4]
    # seconds
    filename = ipstr+'.txt'
    logfile = codecs.open(filename, 'a+', 'utf-8')
    time.sleep(0.1)
    logfile.write("""\
------------------------------------------------
start ping {0} at {1}
if one address were reachable, the response
time(ms) would be record only
------------------------------------------------\n""".format(
        ipstr, nowtime().strftime('%Y-%m-%d %H:%M:%S')))
    time.sleep(0.1)
    cmd = ['ping', '-{}'.format(get_os()[0]), '1400', '-{}'.format(get_os()[2]), ipstr]
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    i = 0
    currentimestr = ''
    thread_start_time = nowtime()
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
                # 获取响应时间，只取数值，其他信息略去
                retime = reline.split(' ')[-2]
                towrite = currentimestr[-8:] + ' ' + retime[used_piece:]
                # linux 平台下处理方式，见下方注释
                # retime = reline.split(' ')[-2]
                # towrite = currentimestr[-8:] + ' ' + retime[5:]
            elif reline.find(u'无法访问' or u'UNREACHABLE') >= 0:
                towrite = currentimestr + ' no response'
            else:
                pass
            logfile.write(towrite+'\n')
            i += 1
        else:
            continue

        delta = int((currentime - thread_start_time).total_seconds())
        # 线程运行的时间，seconds取整数
        if delta % save_interval != 0:
            # 判断时间是否符合条件
            # 根据最后
            continue
        else:
            # 判断是符合退出条件
            logfile.write(currentime.strftime('%Y-%m-%d %H:%M:%S ') + 'data saved\n')
            if delta >= thread_during:
                logfile.write('thread exited')
                logfile.close()
                time.sleep(1)
                QUIT_FLAG = True
            else:
                logfile.close()
                time.sleep(1)
                logfile = codecs.open(filename, 'a', 'utf-8')
    time.sleep(.1)
    popen.kill()
    print (currentimestr + 'thread exited')


def main():
    threads = []
    addrs = IP_ADDRESSES
    for addr in addrs:
        threads.append(threading.Thread(target=monitor, args=(addr,)))
    starttime = datetime.datetime.now()
    print 'multi_pings start at ', starttime.strftime('%Y-%m-%d %H:%M:%S')
    for t in threads:
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()
    endtime = datetime.datetime.now()
    print 'multi_pings end at ', endtime.strftime('%Y-%m-%d %H:%M:%S')

if __name__ == "__main__":
    find_ips()
    time.sleep(5)
    print 'find all ip addresses here: '
    for ip in IP_ADDRESSES:
        print ip
    main()

