import pyautogui
import time

time.sleep(2)

im1 = pyautogui.screenshot(region=(500, 200, 920, 450))
im1.save(r"C:\Users\chooc\PycharmProjects\aimbot_fundamental\savedimage.png")
