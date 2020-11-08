import pyautogui
from pyautogui import *
import time
import random
import keyboard
import win32api
import win32con

# 1st row : X:  489 Y:  901 RGB: ( 78,  81, 116)
# 2nd row : X:  611 Y:  905 RGB: ( 77,  80, 115)
# 3rd row : X:  723 Y:  876 RGB: ( 77,  81, 116)
# 4th row : X:  838 Y:  896 RGB: ( 79,  82, 116)
# Y : 430


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while not keyboard.is_pressed("q"):
    if pyautogui.pixel(489, 430)[0] == 0:
        click(489, 430)
    if pyautogui.pixel(611, 430)[0] == 0:
        click(611, 430)
    if pyautogui.pixel(723, 430)[0] == 0:
        click(723, 430)
    if pyautogui.pixel(838, 430)[0] == 0:
        click(838, 430)


