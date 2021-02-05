import pyautogui, sys, time
print('Press Ctrl-C to quit.')
time.sleep(2)
pyautogui.moveTo(570,250)
time.sleep(1)
pyautogui.hotkey('command','shift','4')
pyautogui.dragTo(1025, 700, 1, button='left')
pyautogui.moveTo(18,255)
#570, 250
#1025, 700
