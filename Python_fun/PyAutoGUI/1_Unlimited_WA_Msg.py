import pyautogui
import time
time.sleep(5)
i = 0
while i<=500:
    pyautogui.typewrite("1000") #Enter yor message here
    pyautogui.press("enter")
    i = i+1