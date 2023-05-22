import pyautogui
import time


pyautogui.alert("The program will start!")
pyautogui.PAUSE = 0.5

name = input("Write an email you wish to search:")
paginas = int(input("Write the number of pages that will be deleted:"))

pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(3)
pyautogui.moveTo(782,584)
pyautogui.click()
time.sleep(3)
pyautogui.hotkey('ctrl','t')
time.sleep(1)
pyautogui.write('gmail.com')
pyautogui.press('enter')
time.sleep(10)
pyautogui.moveTo(435,123)
pyautogui.click()
pyautogui.write(name)
pyautogui.press('enter')
time.sleep(5)
for i in range(0,paginas):
    pyautogui.moveTo(311,235)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(478,233)
    pyautogui.click()
    time.sleep(10)

pyautogui.alert("The program is done!")