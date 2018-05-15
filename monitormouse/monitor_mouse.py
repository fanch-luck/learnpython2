#!/usr/bin/python
# -*- coding:utf-8 -*-
# -----------------------------------------------------------
# File Name: monitor_mouse
# Author:    fan
# date:      2018/2/26
# -----------------------------------------------------------
# coding: utf-8

import pythoncom
import pyHook
import win32api
import win32con
import time
import threading
import random


def send_click():
    global down_num, up_num
    while (1):
        if down_num != up_num:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            # 连射多少秒，大约0.1秒一发子弹
            time.sleep(random.uniform(0.38, 0.42))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
            # 连发之间的停顿时间
            time.sleep(random.uniform(0.25, 0.29))
            print 'click ok'


def onMouse_leftdown(event):
    # 监听鼠标左键按下事件
    global down_num
    down_num += 1
    print "left DOWN DOWN" + str(down_num)
    return True
    # 返回 True 表示响应此事件，False表示拦截


def onMouse_leftup(event):
    # 监听鼠标左键弹起事件
    global up_num
    up_num += 1
    print "left UP UP UP" + str(up_num)
    return True


def main():
    hm = pyHook.HookManager()

    hm.MouseLeftDown = onMouse_leftdown
    hm.MouseLeftUp = onMouse_leftup

    hm.HookMouse()

    # 进入循环，如不手动关闭，程序将一直处于监听状态
    pythoncom.PumpMessages()


if __name__ == "__main__":
    down_num = 0
    up_num = 0
    # 新线程执行的代码:
    print('thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=send_click, name='sendThread')
    t.start()
    # t.join()
    main()
if __name__ == '__main__':
    pass
