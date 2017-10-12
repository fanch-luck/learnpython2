# !user/bin/python
# -*- coding: utf-8 -*-
import platform
import sys
import os
import time
import thread
ip_addresses = []


def get_os():
    currentos = platform.system()
    if currentos == "Windows":
        return "n"
    else:
        return "c"
     

def ping_ip(ip_str):
    cmd = ["ping", "-{op}".format(op=get_os()),
           "1", ip_str]

    output = os.popen(" ".join(cmd)).readlines()
    global ip_addresses
    for line in list(output):
        if not line:
            continue
        if str(line).upper().find("TTL") >= 0:
            print('cmd: ', line[:-1])
            print("ip: %s is ok ***" % ip_str)
            ip_addresses.append(ip_str)
            break


def find_ips(ip_prefix):
    """
    给出当前的127.0.0，然后扫描整个段所有地址
    """
    for i in range(1, 255):
        ip = '%s.%s' % (ip_prefix, i)
        thread.start_new_thread(ping_ip, (ip,))
        time.sleep(0.1)


def savedata(filepath):
    pass

if __name__ == "__main__":
    ip_pre = '192.168.22'
    find_ips(ip_pre)
    time.sleep(20)
    print('find ip addresses:\n', ip_addresses)



