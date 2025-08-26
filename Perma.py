import os
import os, sys
try:import cfonts;from cfonts import render
except:os.system("pip install python-cfonts")
try:import requests
except:os.system("pip install requests")
try:from bs4 import BeautifulSoup
except:os.system("pip install bs4")
try:import json,re,os,sys
except:os.system("pip install json")
try:from datetime import datetime
except:os.system("pip install re")
try:from user_agent import generate_user_agent
except:os.system("pip install user_agent")
try:from user_agent import generate_user_agent as ggb
except:os.system("pip install json")
try:from rich.console import Console
except:os.system("pip install rich")
try:from rich.panel import Panel
except:os.system("pip install threading")
try:import threading,webbrowser
except:os.system("pip install random")
try:import random
except:os.system("pip install hashlib")
try:import hashlib
except:os.system("pip install uuid")
try:import uuid
except:os.system("pip install time")
try:from colorama import Fore, Style
except:os.system("pip install colorama")
import sys
import os, sys, subprocess, importlib.util, time
from requests import post as pp
from random import choice as cc
from random import randrange as rr
import requests
import time, sys, datetime, requests
from colorama import Fore, Style, init
init(autoreset=True)
P = '\x1b[1;97m'
B = '\x1b[1;94m'
O = '\x1b[1;96m'
Z = '\033[1;31m'
X = '\033[1;33m'
F = '\033[2;32m'
L = '\x1b[1;95m'
C = '\033[2;35m'
A = '\033[2;34m'
M = '\x1b[1;37m'
J = '\x1b[38;5;208m'
J1 = '\x1b[38;5;202m'
J2 = '\x1b[38;5;203m'
J21 = '\x1b[38;5;204m'
J22 = '\x1b[38;5;209m'
F1 = '\x1b[38;5;76m'
C1 = '\x1b[38;5;120m'
P1 = '\x1b[38;5;150m'
P2 = '\x1b[38;5;190m'
E = '\033[1;31m'
Y = '\033[1;33m'
Z1 = '\033[2;31m'
S = '\033[2;36m'
G = '\033[1;34m'


def A():
    return random.choice(["cyan", "blue", "green", "yellow", "magenta"])

def B(C, D=0.05):
    for E in C:
        print(E, end='', flush=True)
        time.sleep(D)
    print()

def F():
    from cfonts import render


    # Render PERMA
    perma = render(
        'PERMA',
        font='block',           # You can change to slick or tiny
        colors=['blue', 'green'],
        align='center',
        space=False
    )

    # Render X
    x = render(
        'X',
        font='block',
        colors=['yellow', 'cyan'],
        align='center',
        space=False
    )

    # Render PRAVEEN
    praveen = render(
        'PRAVEEN',
        font='block',
        colors=['blue', 'green'],
        align='center',
        space=False
    )

    # Print them in order
    print(perma)
    print(x)
    print(praveen)

    # Center-aligned Telegram Links
    links = """
          ★ Telegram:@permapy x @pyobscura ✦
          ★ Join Now: @permaera x @praveenbio ✦
    """
    print(links.center(80))  # 80 for approximate center alignment

  
    


F()


total = 0
hits = 0
badinsta = 0
bademail = 0
goodig = 0
b = random.randint(5,208)
bo = f'\x1b[38;5;{b}m'
print("\x1b[1;39m☆" * 60)
Token=input("TOKEN : ")
print("\x1b[1;39m☆" * 60)
ID=input('USER ID: ')    


CHANNEL_1 = "https://t.me/PermaEra"   
CHANNEL_2 = "https://t.me/Praveenfile"  

msg = """🚀 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝗣𝗘𝗥𝗠𝗔 × 𝗣𝗥𝗔𝗩𝗘𝗘𝗡 𝗧𝗼𝗼𝗹 💫  

⚡ 𝗕𝗲𝗳𝗼𝗿𝗲 𝘆𝗼𝘂 𝗰𝗮𝗻 𝘂𝘀𝗲 𝘁𝗵𝗶𝘀 𝘁𝗼𝗼𝗹, 𝗽𝗹𝗲𝗮𝘀𝗲 𝗷𝗼𝗶𝗻 𝗼𝘂𝗿 𝗼𝗳𝗳𝗶𝗰𝗶𝗮𝗹 𝗰𝗵𝗮𝗻𝗻𝗲𝗹𝘀:  
"""

url = f"https://api.telegram.org/bot{Token}/sendMessage"

payload = {
    "chat_id": ID,
    "text": msg,
    "reply_markup": {
        "inline_keyboard": [
            [{"text": "🌌 𝗝𝗼𝗶𝗻 𝗣𝗘𝗥𝗠𝗔 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", "url": CHANNEL_1}],
            [{"text": "🚀 𝗝𝗼𝗶𝗻 𝗣𝗥𝗔𝗩𝗘𝗘𝗡 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", "url": CHANNEL_2}]
        ]
    }
}

try:
    r = requests.post(url, json=payload)
    if r.status_code == 200:
        print(Fore.RED +"✅ FILE EXPIRED!")
    else:
        print(f"❌ Error: {r.text}")
except Exception as e:
    print(f"⚠️ Exception: {e}")


intro_msg = """𝑷𝑬𝑹𝑴𝑨 × 𝑷𝑹𝑨𝑽𝑬𝑬𝑵
🚀  FILE EXPIRED BUY PAID - @PYOBSCURA """

url = f"https://api.telegram.org/bot{Token}/sendMessage"

payload = {"chat_id": ID, "text": intro_msg}
try:
    r = requests.post(url, data=payload)
    if r.status_code == 200:
        print(Fore.GREEN + "✅ FILE EXPIRED!")
    else:
        print(Fore.RED + f"❌ Failed to send message: {r.text}")
except Exception as e:
    print(Fore.RED + f"⚠️ Error: {e}")


print(Fore.CYAN + "FILE EXPIRED\n")
