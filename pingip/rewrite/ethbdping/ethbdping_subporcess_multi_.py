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
import os
import time, datetime
import threading
import thread
import codecs
ip_addresses = []
nowtime = datetime.datetime.now


def find_ips(ip_prefix='192.168.22'):
    """
    给出当前的网段范围，然后扫描整个段所有地址
    """

    def scan_ip(ip_str):
        """
        判断是否ping通，是则加入地址列表
        """
        cmd = ["ping", "-l", "1", ip_str]
        output = os.popen(" ".join(cmd)).readlines()
        global ip_addresses
        time.sleep(.1)
        for line in list(output):
            if not line:
                continue
            if str(line).upper().find("TTL") >= 0:
                ip_addresses.append(ip_str)
                print 'find {}'.format(ip_str)
                break
    for i in xrange(200, 202):
        ip = ip_prefix + '.{}'.format(i)
        thread.start_new_thread(scan_ip, (ip,))
        time.sleep(0.1)


def monitor(ipstr):
    filename = ipstr+'.txt'
    file = codecs.open(filename, 'a+', 'gbk')
    time.sleep(0.1)
    file.write("""\
    ------------------------------------------------
    start ping {0} at {1}
    ------------------------------------------------
    """.format(ipstr, nowtime().strftime('%Y-%m-%d %H:%M:%S')))
    time.sleep(0.1)
    cmd = ['ping', ipstr, '-l', '1400', '-t']
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE)

    while True:
        ctime = nowtime()
        line = popen.stdout.readline()
        if line:
            reline = line[:-2].decode('gbk').upper()
            towrite = ''
            if reline.upper().find('PING') >= 0:
                towrite = '{} '.format(ctime.strftime('%Y-%m-%d %H:%M:%S ')) + reline[:-1]
            elif reline.upper().find('TTL') >= 0:
                towrite = '{} '.format(ctime.strftime('%H:%M:%S ') + 'response time {}'.format(reline[33:-9]))
            elif reline.find(u'无法访问'):
                towrite = '{} '.format(ctime.strftime('%Y-%m-%d %H:%M:%S ')) + 'no response'
            else:
                continue
            file.write(towrite+'\n')
        else:
            continue
        if nowtime().strftime('%Y%m%d%H%M%S')[-2:] != '00':
            continue
        else:
            file.write(ctime.strftime('%Y-%m-%d %H:%M:%S ') + 'data saved\n')
            file.close()
            time.sleep(1)
            file = codecs.open(filename, 'a', 'gbk')
            time.sleep(.1)


def main():
    global ip_addresses
    threads = []
    addrs = ip_addresses
    for addr in addrs:
        threads.append(threading.Thread(target=monitor, args=(addr,)))
    starttime = datetime.datetime.now()
    print('start at ', starttime.strftime('%Y-%m-%d %H:%M:%S'))
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()
    endtime = datetime.datetime.now()
    print('end at ', endtime.strftime('%Y-%m-%d %H:%M:%S'))

if __name__ == "__main__":
    find_ips()
    time.sleep(5)
    print 'find all ip addresses here: '
    for ip in ip_addresses:
        print ip
    main()

