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

(!) BLIXTEN37 DOES NOT OWE YOU SOMETHING IF YOUR COMPUTER BREAKS (!)

"""
PREFIX = str("[TSB]")
NAME = str("Text Spam Script")
VERSION = str("0.0.1")
CREATOR = str("Blixten37")
LICENSE = str("MIT License")

print(f"--~~ [ {NAME} ] ~~--")
print(""), print("This bot is under the MIT License, read more at: https://en.wikipedia.org/wiki/MIT_License")
print(""), print("DiscordSpamBotScript (C) 2021 Blixten37"), print("")
print(f"Name: {NAME}")
print(f"Version: {VERSION}")
print(f"Creator: {CREATOR}")
print(f"License: {LICENSE}")
print("")

import random

print(f"{PREFIX} | INFO: Successfully imported random")
import pyautogui

print(f"{PREFIX} | INFO: Successfully imported pyautogui")
import time

print(f"{PREFIX} | INFO: Successfully imported time")
import tkinter as tk

print(f"{PREFIX} | INFO: Successfully imported tkinter"), print("")

root = tk.Tk()
root.title("Text Spam Bot")

loop = bool(False)


def onEnable():
    loop = bool(True)
    print(f"{PREFIX} | INFO: Enabled spam")
    f = open("spam", "r")

    for word in f:
        while loop == bool(True):
            time.sleep(1)

            pyautogui.typewrite(random.choice(open("spam").read().split(), )), pyautogui.typewrite(" ")

            pyautogui.typewrite(random.choice(open("spam").read().split(), )), pyautogui.typewrite(" ")

            pyautogui.typewrite(random.choice(open("spam").read().split(), )), pyautogui.typewrite(" ")

            pyautogui.typewrite(random.choice(open("spam").read().split(), )), pyautogui.typewrite(" ")

            pyautogui.typewrite(random.choice(open("spam").read().split(), )), pyautogui.typewrite(" ")

            pyautogui.press("enter")

        if loop == bool(False):
            onDisable()

        else:
            print(f"{PREFIX} | ERROR/main.py: Error ")


def onDisable():
    loop = bool(False)
    print(f"{PREFIX} | INFO: Disabled spam")


# -------- GUI -------- #

# Labels
Lb1 = tk.Label(root, text="Spam Script", ).pack()

# Empty
Em1 = tk.Label(root, text="    ").pack()

# Buttons
BtnStart = tk.Button(root, text="Start", command=onEnable,
                     # Style | BtnStart
                     padx=20, pady=5).pack()

BtnStop = tk.Button(root, text="Stop", command=onDisable,
                    # Style | BtnStop
                    padx=20, pady=5).pack()

# Quit
root.mainloop()
print(f"{PREFIX} | INFO/main.py: Script closed")
quit()
