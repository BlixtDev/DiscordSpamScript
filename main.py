import tkinter as tk
import time
import pyautogui
import random
print("--~~ [ Text Spam Bot ] ~~--")
print(""), print(
    "This bot is under the MIT License, read more at: https://en.wikipedia.org/wiki/MIT_License")
print(""), print("DiscordSpamBotScript (C) 2021 Blixten37"), print("")


print("[TSB] | INFO: Successfully imported random")

print("[TSB] | INFO: Successfully imported pyautogui")

print("[TSB] | INFO: Successfully imported time")

print("[TSB] | INFO: Successfully imported tkinter"), print("")

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
    loop = "false"
    print("Disabled spam")


Btn1 = tk.Button(root, text="Start", command=onEnable).pack()
Btn2 = tk.Button(root, text="Stop", command=onDisable).pack()


root.mainloop()
