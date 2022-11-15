from pyautogui import *
from multiprocessing import Process
import pyautogui
import time
import keyboard
import win32api, win32con
import os   
       
def lclick(x,y):
    win32api.SetCursorPos((x,y))
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)      

time.sleep(2.5)
print("now")
i = 0
while(not(keyboard.is_pressed('ctrl'))):   
    if (pyautogui.pixel(777, 457)[0] == 56):
        #time.sleep(0.1)
        lclick(777,497)
        time.sleep(0.05)
        win32api.SetCursorPos((60,500))
    if (pyautogui.pixel(832, 457)[0] == 56):
        #time.sleep(0.1)
        lclick(832,497)
        time.sleep(0.05)
        win32api.SetCursorPos((60,500))
    if (pyautogui.pixel(886, 457)[0] == 56):
        #time.sleep(0.1)
        lclick(886,497)
        time.sleep(0.05)
        win32api.SetCursorPos((60,500))
    if (pyautogui.pixel(940, 457)[0] == 56):
        #time.sleep(0.1)
        lclick(940,497)
        time.sleep(0.05)
        win32api.SetCursorPos((60,500))
    if (pyautogui.pixel(993, 457)[0] == 56):
        #time.sleep(0.1)
        lclick(993,497)
        time.sleep(0.05)
        win32api.SetCursorPos((60,500))
    if (pyautogui.pixel(1047, 457)[0] == 56):
        #time.sleep(0.1)
        lclick(1047,497)
        time.sleep(0.05)
        win32api.SetCursorPos((60,500))
    if (pyautogui.pixel(1100, 457)[0] == 56):
        #time.sleep(0.1)
        lclick(1100,497)
        time.sleep(0.05)
        win32api.SetCursorPos((60,500))

