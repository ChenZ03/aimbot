import pyautogui
from pyautogui import *
import time
import random
import keyboard
import win32api
import win32con

X = 823
Y = 364
G = 150


while not keyboard.is_pressed("q"):
    if pyautogui.pixel(X, Y)[1] > G:
        win32api.SetCursorPos((X, Y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.03)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
