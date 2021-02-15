from twill.commands import go

print("--~~ [ Discord Spam Bot Script ] ~~--")
print(""), print("This bot is under the MIT License, read more at: https://en.wikipedia.org/wiki/MIT_License")
print(""), print("DiscordSpamBotScript (C) 2021 Blixten37"), print("")

import os
print("[DSBS] | INFO: Succesfully imported os")
import sys
print("[DSBS] | INFO: Succesfully imported sys")
import random
print("[DSBS] | INFO: Succesfully imported random")
import json
print("[DSBS] | INFO: Succesfully imported json")
import requests
print("[DSBS] | INFO: Succesfully imported requests")
import pyautogui
print("[DSBS] | INFO: Succesfully imported pyautogui")
import time
print("[DSBS] | INFO: Succesfully imported time"), print("")


time.sleep(1), print("1")

time.sleep(1), print("2")

time.sleep(1), print("3")

time.sleep(1), print("4")

time.sleep(1), print("5")

time.sleep(1), print("GOOOOOO!"), print("")

f = open("spam", "r")

loop = "true"

for word in f:
    while loop == "true":
        time.sleep(1)
        pyautogui.typewrite(random.choice(open("spam").read().split(),))
        pyautogui.typewrite(" ")

        pyautogui.typewrite(random.choice(open("spam").read().split(),))
        pyautogui.typewrite(" ")

        pyautogui.typewrite(random.choice(open("spam").read().split(),))
        pyautogui.typewrite(" ")

        pyautogui.typewrite(random.choice(open("spam").read().split(),))
        pyautogui.typewrite(" ")

        pyautogui.press("enter"), print(f"sent some spam!")
