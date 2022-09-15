# >>> Discord webhook spammer
# >>> github.com/SecretDev1111/Discord-Webhook-Spammer

import time
from tkinter import Y
import requests
from colorama import Fore
import socket

import os
os.system("cls")

import ctypes
from re import I, X
ctypes.windll.kernel32.SetConsoleTitleW("Discord Webhook Spammer")

class color:
    light = "\033[1m"
    
def main():
    print(color.light, Fore.GREEN + """
| 
| ░██╗░░░░░░░██╗███████╗██████╗░░██████╗██████╗░░█████╗░███╗░░░███╗███╗░░░███╗███████╗██████╗░
| ░██║░░██╗░░██║██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗████╗░████║████╗░████║██╔════╝██╔══██╗
| ░╚██╗████╗██╔╝█████╗░░██████╦╝╚█████╗░██████╔╝███████║██╔████╔██║██╔████╔██║█████╗░░██████╔╝
| ░░████╔═████║░██╔══╝░░██╔══██╗░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██╔══██╗
| ░░╚██╔╝░╚██╔╝░███████╗██████╦╝██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║██║░╚═╝░██║███████╗██║░░██║
| ░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝
|
| >> github.com/SecretDev1111/Discord-Webhook-Spammer
| >> TO STOP THE SPAMMER JUST CLOSE THE WINDOW
|
    """)
print()
main()    
msg = input("Message: ")
webhook = input("Webhook URL: ")
start = input("Click ENTER to start spammer... ")

def spam(msg, webhook):
    while True:
        try:
            data = requests.post(webhook, json={'content': msg})
            print(Fore.RED + """
            >>> MESSAGE SENT!
            >>> TO STOP THE SPAMMER JUST CLOSE THE WINDOW.
            """)
        except:
            os.system("cls")
            print(Fore.RED + """
                  
| 
| ░██╗░░░░░░░██╗███████╗██████╗░░██████╗██████╗░░█████╗░███╗░░░███╗███╗░░░███╗███████╗██████╗░
| ░██║░░██╗░░██║██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗████╗░████║████╗░████║██╔════╝██╔══██╗
| ░╚██╗████╗██╔╝█████╗░░██████╦╝╚█████╗░██████╔╝███████║██╔████╔██║██╔████╔██║█████╗░░██████╔╝
| ░░████╔═████║░██╔══╝░░██╔══██╗░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██╔══██╗
| ░░╚██╔╝░╚██╔╝░███████╗██████╦╝██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║██║░╚═╝░██║███████╗██║░░██║
| ░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝
|
| >> github.com/SecretDev1111/Discord-Webhook-Spammer
| >> TO STOP THE SPAMMER JUST CLOSE THE WINDOW
|




                  
ERROR with webhook. The window is about to close.
                
                """)
            time.sleep(5)
            exit()

spammer = 1
while spammer == 1:
    spam(msg, webhook)