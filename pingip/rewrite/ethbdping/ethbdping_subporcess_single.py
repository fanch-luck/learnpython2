#!/usr/bin/python
# -*- coding:utf-8 -*-
# -----------------------------------------------------------
# File Name：     ethbdping_subporcess_single.py
# Description :
#   Author:      fan
#   date:        2017/10/11
#   IDE:         PyCharm Community Edition
# -----------------------------------------------------------

import subprocess
import time


def ping_ip(ipstr):
    # cmd = ["ping", "-{op}".format(op=get_os()),
    #        "10", ip_str]
    file = open(ipstr+'.txt', 'w+')
    cmd = ['ping', ipstr, '-n', '10']
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    start = time.clock()
    while time.clock()-start < 1:
        line = popen.stdout.readline()
        if line:
            file.write(line[:-1].decode('gbk'))


if __name__ == "__main__":
    addr = '192.168.22.200'
    ping_ip(addr)

