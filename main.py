print("--~~ [ Text Spam Bot ] ~~--")
print(""), print("This bot is under the MIT License, read more at: https://en.wikipedia.org/wiki/MIT_License")
print(""), print("DiscordSpamBotScript (C) 2021 Blixten37"), print("")

import random
print("[TSB] | INFO: Succesfully imported random")
import pyautogui
print("[TSB] | INFO: Succesfully imported pyautogui")
import time
print("[TSB] | INFO: Succesfully imported time")
import tkinter as tk
print("[TSB] | INFO: Succesfully imported tkinter"), print("")

root = tk.Tk()
root.title("Text Spam Bot")

loop = "false"

def onEnable():
    loop = "true"
    print("Enabled spam")
    f = open("spam", "r")

    for word in f:
        while loop == "true":
            time.sleep(1)
            pyautogui.typewrite(random.choice(open("spam").read().split(),)), pyautogui.typewrite(" ")

            pyautogui.typewrite(random.choice(open("spam").read().split(),)), pyautogui.typewrite(" ")

            pyautogui.typewrite(random.choice(open("spam").read().split(),)), pyautogui.typewrite(" ")

            pyautogui.typewrite(random.choice(open("spam").read().split(),)), pyautogui.typewrite(" ")

            pyautogui.typewrite(random.choice(open("spam").read().split(),)), pyautogui.typewrite(" ")

            pyautogui.press("enter")


def onDisable():
    loop = "false"
    print("Disabled spam")

Btn1 = tk.Button(root, text="Start", command=onEnable)
Btn2 = tk.Button(root, text="Stop", command=onDisable)

Btn1.pack()
Btn2.pack()
root.mainloop()