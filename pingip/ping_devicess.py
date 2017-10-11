# !user/bin/python
# -*- coding: utf-8 -*-
import platform
import sys
import os
import time
import _thread as thread
ip_addresses = []
ping_result_data = []
ping_result_time = []


def get_os():
    """
    get os 类型
    """
    os = platform.system()
    if os == "Windows":
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
            print(line[:-1])
            print("ip: %s is ok ***" % ip_str)
            ip_addresses.append(ip_str)
            break


def test_ip(ip_addr, count=100, lenth=1024):
    """
    对单个IP地址进行检测
    :param ip_addr: ip地址字符串
    :param count: 发送次数
    :param lenth: 包长度
    :return:
    """
    global ping_result_time
    global ping_result_data
    cmd = ['ping', '-{op}'.format(op=get_os()), str(count), '-l', str(lenth), ip_addr]
    output = os.popen(' '.join(cmd)).readlines()
    # output = os.popen('ping -n 180 -l 1024 192.168.22.200').readlines()
    time.sleep(2)
    print('cmd: ', output[-4:])

def find_ips(ip_prefix):
    """
    给出当前的127.0.0，然后扫描整个段所有地址
    """
    for i in range(1, 255):
        ip = '%s.%s' % (ip_prefix, i)
        thread.start_new_thread(ping_ip, (ip,))
        time.sleep(0.1)


def check_ips(ips):
    for ip in ips:
        thread.start_new_thread(test_ip, (ip, 180, 1024))
        time.sleep(0.2)

if __name__ == "__main__":
    ip_prefix = '192.168.22'
    find_ips(ip_prefix)



