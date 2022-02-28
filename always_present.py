                                    ####################################################################################
                                    ####################################################################################
                                    ####                                                                            ####
                                    ####                                                                            ####
                                    ####                #   Mohamed Menfalouti                                      ####
                                    ####                #   github : MeedMn                                         ####
                                    ####                #   instagram : meedmen01                                   ####
                                    ####                #   facebook : mohamed menfalouti                           ####
                                    ####                #   LinkedIn : mohamed menfalouti                           ####
                                    ####                                                                            ####
                                    ####                                                                            ####
                                    ####################################################################################
                                    ####################################################################################

import win32api, win32con
import pyautogui as pg
from pynput.mouse import Controller,Listener
import schedule
import time
import speech_recognition as sr
import sys

r = sr.Recognizer()
m = sr.Microphone(device_index=0)

#to get the position of input
print("Click the position where you want to type !")

def is_clicked(x, y, button, pressed):
    if pressed:
        global current_mouse_position
        mouse = Controller()
        current_mouse_position = mouse.position
        return False

with Listener(on_click=is_clicked) as listener:
    listener.join()

choice = input("Enter your name : ")

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    win32api.SetCursorPos((x, y))

#to go to the position of input
click(current_mouse_position[0],current_mouse_position[1])

def job():
    with m as source:
        audio = r.listen(source)
    result = r.recognize_google(audio)
    print(result)
    if choice.lower() in result.lower():
        pg.write("Present")
        pg.typewrite(["enter"])
        sys.exit()
schedule.every(1).seconds.do(job)
while 1:
    schedule.run_pending()
    time.sleep(1)