"""
~~-- MIT LICENSE --~~

Copyright (c) 2021 Blixten37

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

import tkinter as tk
import time
import pyautogui
import random
print("--~~ [ Text Spam Bot ] ~~--")
print(""), print(
    "This bot is under the MIT License, read more at: https://en.wikipedia.org/wiki/MIT_License")
print(""), print("DiscordSpamBotScript (C) 2021 Blixten37"), print("")

PREFIX = "[TSB]"


print(f"{PREFIX} | INFO: Successfully imported random")

print(f"{PREFIX} | INFO: Successfully imported pyautogui")

print(f"{PREFIX} | INFO: Successfully imported time")

print(f"{PREFIX} | INFO: Successfully imported tkinter"), print("")

root = tk.Tk()
root.title("Text Spam Bot")

loop = False


def onEnable():
    loop = True
    print(f"{PREFIX} | INFO: Enabled spam")
    f = open("spam", "r")

    for word in f:
        while loop == True:

            time.sleep(1)

            pyautogui.typewrite(random.choice(
                open("spam").read().split(), )), pyautogui.typewrite(" ")

            pyautogui.typewrite(random.choice(
                open("spam").read().split(), )), pyautogui.typewrite(" ")

            pyautogui.typewrite(random.choice(
                open("spam").read().split(), )), pyautogui.typewrite(" ")

            pyautogui.typewrite(random.choice(
                open("spam").read().split(), )), pyautogui.typewrite(" ")

            pyautogui.typewrite(random.choice(
                open("spam").read().split(), )), pyautogui.typewrite(" ")

            pyautogui.press("enter")


def onDisable():
    loop = False
    print(f"{PREFIX} | INFO: Disabled spam")


# -------- GUI -------- #

# Labels
Lb1 = tk.Label(root, text="Spam Script", ).pack()

# Empty
Em1 = tk.Label(root, text="    ").pack()

# Buttons
Btn1 = tk.Button(root, text="Start", command=onEnable,
                 # Style | Btn1
                 padx=20, pady=5).pack()

Btn2 = tk.Button(root, text="Stop", command=onDisable,
                 # Style | Btn1
                 padx=20, pady=5).pack()

# Quit
root.mainloop()
print(f"{PREFIX} | INFO/main.py: Script closed")
quit()
