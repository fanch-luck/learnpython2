#!/usr/bin/python
# -*- coding:utf-8 -*-
# -----------------------------------------------------------
# File Name: monitor__mouse
# Author:    fan
# date:      2018/2/26
# -----------------------------------------------------------
# -*- coding: utf-8 -*-
import pythoncom
import pyHook


def OnMouseEvent(event):
    print 'MessageName:', event.MessageName
    print 'Message:', event.Message
    print 'Time:', event.Time
    print 'Window:', event.Window
    print 'WindowName:', event.WindowName
    print 'Position:', event.Position
    print 'Wheel:', event.Wheel
    print 'Injected:', event.Injected
    print '---'
    # 返回 True 可将事件传给其它处理程序，否则停止传播事件
    return True

if __name__ == '__main__':
    # 创建钩子管理对象
    hm = pyHook.HookManager()
    # 监听所有鼠标事件
    #  等效于hm.SubscribeMouseAll(OnMouseEvent)
    hm.MouseAll = OnMouseEvent
    # 开始监听鼠标事件
    hm.HookMouse()
    # 一直监听，直到手动退出程序
    pythoncom.PumpMessages()

