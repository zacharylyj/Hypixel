from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con  
       
def lclick(x,y):
    win32api.SetCursorPos((x,y))
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)      

def rclick(x,y):
    win32api.SetCursorPos((x,y))
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)  

def aimbot():
    if (pyautogui.pixel(777, 412)[0] == 56):
        #time.sleep(0.1)
        lclick(777,497)
        time.sleep(0.1)
        win32api.SetCursorPos((60,500))
    if (pyautogui.pixel(832, 412)[0] == 56):
        #time.sleep(0.1)
        lclick(832,497)
        time.sleep(0.1)
        win32api.SetCursorPos((60,500))
    if (pyautogui.pixel(886, 412)[0] == 56):
        #time.sleep(0.1)
        lclick(886,497)
        time.sleep(0.1)
        win32api.SetCursorPos((60,500))
    if (pyautogui.pixel(940, 412)[0] == 56):
        #time.sleep(0.1)
        lclick(940,497)
        time.sleep(0.1)
        win32api.SetCursorPos((60,500))
    if (pyautogui.pixel(993, 412)[0] == 56):
        #time.sleep(0.1)
        lclick(993,497)
        time.sleep(0.1)
        win32api.SetCursorPos((60,500))
    if (pyautogui.pixel(1047, 412)[0] == 56):
        #time.sleep(0.1)
        lclick(1047,497)
        time.sleep(0.1)
        win32api.SetCursorPos((60,500))
    if (pyautogui.pixel(1100, 412)[0] == 56):
        #time.sleep(0.1)
        lclick(1100,497)
        time.sleep(0.1)
        win32api.SetCursorPos((60,500))



time.sleep(4)
print("now")
while(not(keyboard.is_pressed('ctrl'))):
    time.sleep(1)
    rclick(960,524)
    time.sleep(1)
    rclick(1060,400)
    time.sleep(1)
    while((pyautogui.pixel(1200, 500)[0] == 56) and not(keyboard.is_pressed('ctrl'))):
        aimbot()
      
