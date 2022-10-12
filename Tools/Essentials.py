#The EnDa Password Generator's Essentials module

#Import needed modules
import os
from colorama import Fore
from pystyle import Colors, Colorate
import requests
import random
import time
import string
import secrets
import pyperclip

#Create needed values
global value
value = random.randint(1,4)

#Define an space function
def space():
    print()

#Define a clear terminal function
def clearConsole():
    command = "clear"
    if os.name in ("dos",'nt'):
        command = "cls"
    os.system(command)

#Define an error function
def error(string):
    print(Fore.RED + "[ERROR]" + Fore.WHITE + " >> " + Fore.LIGHTBLACK_EX + str(string))

#Define a banner function
def banner(option):
    if int(option) == 1:
        print(Colorate.Vertical(Colors.white_to_red,r"""
 _____     ______       ______                                   _   _____                           _             
|  ___|    |  _  \      | ___ \                                 | | |  __ \                         | |            
| |__ _ __ | | | |__ _  | |_/ /_ _ ___ _____      _____  _ __ __| | | |  \/ ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
|  __| '_ \| | | / _` | |  __/ _` / __/ __\ \ /\ / / _ \| '__/ _` | | | __ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
| |__| | | | |/ / (_| | | | | (_| \__ \__ \\ V  V / (_) | | | (_| | | |_\ \  __/ | | |  __/ | | (_| | || (_) | |   
\____/_| |_|___/ \__,_| \_|  \__,_|___/___/ \_/\_/ \___/|_|  \__,_|  \____/\___|_| |_|\___|_|  \__,_|\__\___/|_|                                                                                                                                                                                                                                            
        """,1))
    elif int(option) == 2:
        print(Colorate.Vertical(Colors.yellow_to_red,"""
            (             (                                                                                                
            )\ )          )\ )                                  (      (                                       )           
 (         (()/(      )  (()/(    )          (  (         (     )\ )   )\ )      (           (   (       )  ( /(      (    
 )\    (    /(_))  ( /(   /(_))( /(  (   (   )\))(    (   )(   (()/(  (()/(     ))\  (      ))\  )(   ( /(  )\()) (   )(   
((_)   )\ )(_))_   )(_)) (_))  )(_)) )\  )\ ((_)()\   )\ (()\   ((_))  /(_))_  /((_) )\ )  /((_)(()\  )(_))(_))/  )\ (()\  
| __| _(_/( |   \ ((_)_  | _ \((_)_ ((_)((_)_(()((_) ((_) ((_)  _| |  (_)) __|(_))  _(_/( (_))   ((_)((_)_ | |_  ((_) ((_) 
| _| | ' \))| |) |/ _` | |  _// _` |(_-<(_-<\ V  V // _ \| '_|/ _` |    | (_ |/ -_)| ' \))/ -_) | '_|/ _` ||  _|/ _ \| '_| 
|___||_||_| |___/ \__,_| |_|  \__,_|/__//__/ \_/\_/ \___/|_|  \__,_|     \___|\___||_||_| \___| |_|  \__,_| \__|\___/|_|                                                                                                                                     
        """,1))
    elif int(option) == 3:
        print(Colorate.Vertical(Colors.red_to_white,"""
▒█▀▀▀ █▀▀▄ ▒█▀▀▄ █▀▀█ 　 ▒█▀▀█ █▀▀█ █▀▀ █▀▀ █░░░█ █▀▀█ █▀▀█ █▀▀▄ 　 ▒█▀▀█ █▀▀ █▀▀▄ █▀▀ █▀▀█ █▀▀█ ▀▀█▀▀ █▀▀█ █▀▀█ 
▒█▀▀▀ █░░█ ▒█░▒█ █▄▄█ 　 ▒█▄▄█ █▄▄█ ▀▀█ ▀▀█ █▄█▄█ █░░█ █▄▄▀ █░░█ 　 ▒█░▄▄ █▀▀ █░░█ █▀▀ █▄▄▀ █▄▄█ ░░█░░ █░░█ █▄▄▀ 
▒█▄▄▄ ▀░░▀ ▒█▄▄▀ ▀░░▀ 　 ▒█░░░ ▀░░▀ ▀▀▀ ▀▀▀ ░▀░▀░ ▀▀▀▀ ▀░▀▀ ▀▀▀░ 　 ▒█▄▄█ ▀▀▀ ▀░░▀ ▀▀▀ ▀░▀▀ ▀░░▀ ░░▀░░ ▀▀▀▀ ▀░▀▀
        """,1))
    elif int(option) == 4:
        print(Colorate.Vertical(Colors.blue_to_red,"""                                                                                                   
 _____     ____         _____                             _    _____                     _           
|   __|___|    \ ___   |  _  |___ ___ ___ _ _ _ ___ ___ _| |  |   __|___ ___ ___ ___ ___| |_ ___ ___ 
|   __|   |  |  | .'|  |   __| .'|_ -|_ -| | | | . |  _| . |  |  |  | -_|   | -_|  _| .'|  _| . |  _|
|_____|_|_|____/|__,|  |__|  |__,|___|___|_____|___|_| |___|  |_____|___|_|_|___|_| |__,|_| |___|_|                                                                                                               
        """,1))
    else:
        error("The option about banner printing is not avaible!")
        time.sleep(10)
        exit()