#!/usr/bin/python
# -*- coding:utf-8 -*-
# -----------------------------------------------------------
# File Name: monitormouse
# Author:    fan
# date:      2018/2/26
# -----------------------------------------------------------
import pythoncom
import pyHook
def onMouseEvent(event):
     print "Position:", event.Position
     return True
def main():
    hm = pyHook.HookManager()
    hm.HookKeyboard()
    hm.MouseAll = onMouseEvent
    hm.HookMouse()
    pythoncom.PumpMessages()
if __name__ == "__main__":
    main()
if __name__ == '__main__':
    pass
