#usr/bin/python3 !
# the powerful in the internet the Mr Root / my friend [MJi]
#---------------------
import sys
from time import sleep
from os import system
#---------------------
try:
    import requests
except:
    try:
        system('pip install requests')
    except:
        system('pip3 install requests')
try:
    import datetime
except:
    try:
        system('pip install datetime')
    except:
        system('pip3 install datetime')
try:
    import flags
except:
    system("pip install flags")
#--------------------
try:
    from colorama import Fore
except:
    system("pip install colorama")
try:
    import colored
except:
    system("pip install colored")
#----
from colored import fg, bg, attr #background
import flags,requests
from colorama import Fore
#try:
    #system('pkg install sox -y')
#except:
    #None
    
#import MySql
#---------------------
# the   # color----
class color:
    CYAN = '\033[96m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDER = '\033[4m'
    blue = "\033[36m"
    PINK = "\033[35m"
    DARKBLUE = "\033[34m"
    WHITE = "\033[00m"
#---------
tim = (datetime.datetime.today())

name = sys.argv[1]
password = sys.argv[2]
target = sys.argv[3]
if password == "rootcode":
    sleep(1)
    enter = input(Fore.RED+F'[{name}]'+Fore.BLUE+" - "+Fore.GREEN+F"[{tim}]"+Fore.WHITE+' | enter username root ? [y|n] >> ')
    print()
    if enter == "y".lower():
        user = input(F"{color.WHITE}[{name}] - {color.GREEN}[{tim}] | {color.YELLOW}enter your username vip {color.BLUE} >>{color.GREEN} ")
        print()
        if user == "allroot".lower():
            ps = input(F"{color.YELLOW}enter your password vip {color.BLUE}⟩⟩{color.GREEN} ")
            print()
            if ps == "rooted".lower():
                sleep(1)
                print(F'\n{color.BLUE}user and password {color.RED}(allroot@rooted) {color.GREEN}[found]\n\n')
                sleep(1)
                # flags
                print(F"\r {color.PINK}[]                                         ",end="",flush=False)
                print ('\n\n')
                print(f"\r{color.RED}logging in to VIP..",end="",flush=False)
                sleep(1)
                print(f"\r{color.RED}logging in to VIP....",end="",flush=False)
                sleep(1)
                print(f"\r{color.RED}logging in to VIP......",end="",flush=False)
                sleep(1)
                print(f"\r{color.RED}logging in to VIP........",end="",flush=False)
                sleep(1)
                print(f"\r{color.RED}logging in to VIP..........",end="",flush=False)
                sleep(2)
                try:
                    system("cd && git clone https://github.com/Mester-Root/code && cd code && chmod 777 * && python the")
                except:
                    system("cd $HOME")
                    system("git clone https://github.com/Mester-Root/code")
                    system("cd code")
                    system("chmod +x *")
                    system("python the")
            else:
                print(f"{color.RED}[SORRY]:\n{color.PINK}password not found")
                
        if user == "mmdroot".lower():
            pss = input(F"{color.YELLOW}enter your password vip {color.BLUE}⟩⟩{color.GREEN} ")
            if pss == "rooted".lower():
                sleep(1)
                print(F'\n{color.BLUE}user and password {color.RED}(mmdroot@rooted) {color.GREEN}[found]\n\n')
                sleep(1)
                # flags
                print(F"\r {color.PINK}[]                                         ",end="",flush=False)
                print ('\n\n')
                print(f"\r{color.RED}logging in to VIP..",end="",flush=False)
                sleep(1)
                print(f"\r{color.RED}logging in to VIP....",end="",flush=False)
                sleep(1)
                print(f"\r{color.RED}logging in to VIP......",end="",flush=False)
                sleep(1)
                print(f"\r{color.RED}logging in to VIP........",end="",flush=False)
                sleep(1)
                print(f"\r{color.RED}logging in to VIP..........",end="",flush=False)
                sleep(2)
                try:
                    system("cd && git clone https://github.com/Mester-Root/code && cd code && chmod 777 * && python the")
                except:
                    system("cd $HOME")
                    system("git clone https://github.com/Mester-Root/code")
                    system("cd code")
                    system("chmod +x *")
                    system("python the")
            else:
                print(f"{color.RED}[SORRY]:\n{color.PINK}password not found")
    if enter == "n".lower():
        print('\n~\n')
    sleep(1)
    #--------
    try:
        system('clear')
    except:
        system('cls')
    #--------

    sleep(0.5)
    try:
        system('clear')
    except:
        system('cls')
    tim = (datetime.datetime.today())
    te = requests.get("https://api.codebazan.ir/time-date/?td=all").text
    sleep(1)
    banner = (F"""\n{color.YELLOW}
         {color.GREEN} -[{name}]-{color.YELLOW}

              _________      
_____________ ______  /_____ 
_  ___/_  __ \_  __  / _  _ \
/ /__  / /_/ // /_/ /  /  __/{color.CYAN}
\___/  \____/ \__,_/   \___/ 
                             
                             
{color.BLUE}[{te}]


"""+F"""{color.RED}
________________________\n"""+Fore.BLUE+'''
[to enter the directory]'''+F"""

{color.YELLOW}[{color.GREEN}tyep{color.YELLOW}] {color.BLUE}="""+Fore.WHITE+''' /account/code/'''+F"""

{color.YELLOW}[{color.GREEN}type{color.YELLOW}] {color.BLUE}="""+Fore.WHITE+''' /channel/code/'''+F"""

{color.YELLOW}[{color.GREEN}type{color.YELLOW}] {color.BLUE}="""+Fore.WHITE+''' /group/code/'''+F"""{color.RED}

————————————————————————\n

{color.GREEN}[{tim}] {color.YELLOW}> {color.RED}root@terminal~:/code/# {color.BLUE}─╼ ❯❯❯"""+Fore.WHITE +''' ''')

    for bnr in banner:
        sys.stdout.write(bnr)
        sys.stdout.flush()
        sleep(0.01)
    code = input()
    sleep(2) 
    # Method 1 ----
    system("clear")
    if code == '/account/code/':
        print(f'{color.RED}\nreporter: ({name})\n\n')
        sleep(0.7)
        print(f'{color.GREEN}----------------------\n')
        cood = requests.get("https://raw.githubusercontent.com/Mester-Root/code/main/code.txt").text
        #
        sleep(0.6)
        print(F'''{color.YELLOW}'''+cood)
        sleep(0.5)
        print(f'\n{color.GREEN}--------------------')
        print(F'\n{color.WHITE}send to {color.RED}[{target}]')
        print(f'\n[{color.PINK}{tim}]')
        # method 2 -----
    elif code == "/channel/code/".lower():
        print(f'{color.RED}\nreporter: ({name})\n\n')
        sleep(0.7)
        print(f'{color.GREEN}----------------------\n')
        cood = requests.get("https://raw.githubusercontent.com/Mester-Root/code/main/cood.txt").text
        sleep(0.6)
        print(F'''{color.YELLOW}'''+cood)
        sleep(0.5)
        print(f'\n{color.GREEN}--------------------')
        print(F'\n{color.WHITE}send to {color.RED}[{target}]')
        print(f'\n[{color.PINK}{tim}]')
        # --- method 3 ----
    elif code == "/group/code/".lower():
        print(f'{color.RED}\nreporter: ({name})\n\n')
        sleep(0.7)
        print(f'{color.GREEN}----------------------\n')
        cood = requests.get("https://raw.githubusercontent.com/Mester-Root/code/main/cod.txt").text
        sleep(0.6)
        print(F'''{color.YELLOW}'''+cood)
        sleep(0.5)
        print(f'\n{color.GREEN}--------------------')
        print(F'\n{color.WHITE}send to {color.RED}[{target}]')
        print(f'\n[{color.PINK}{tim}]')
        #---
# ------- the end ------
else:
    print(f"{color.RED}\npassword not found")
print()
sleep(3)
input(Fore.WHITE+"[music] "+Fore.RED+"(enter) ⟩⟩")
try:
    system("play khalvat.mp3 &> /dev/null")
except:
    system("pkg install sox")
#----- finished ------
sys.exit()