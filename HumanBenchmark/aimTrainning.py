import pyautogui
from pyautogui import *
import time
import random
import keyboard
import win32api
import win32con

time.sleep(2)

# Target X:  951 Y:  387 RGB: (149, 195, 232)
# region=(500, 200, 920, 450)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.03)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


n = 0
while not keyboard.is_pressed("s"):
    ss = pyautogui.screenshot(region=(500, 205, 920, 450))
    width, height = ss.size
    for x in range(0, width, 55):
        for y in range(0, height, 55):

            r, g, b = ss.getpixel((x, y))
            if r in range(149, 200):

                click(x+500, y+205)
                n += 1
                time.sleep(0.04)
                break

