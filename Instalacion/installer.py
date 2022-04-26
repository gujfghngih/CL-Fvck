import os
import time
import datetime
from termcolor import colored

colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta','\x1b[38;5;206m']
#################################################################################  Definicion del Tiempo
date = datetime.datetime.now()
timed = date.strftime("%d\%m\%Y")
################################################################################# TMP

from colorama import *
################################################################################# CLA

clear = lambda: os.system('cls') if os.name == 'nt' else os.system('clear')
#################################################################################  Clear
def close():
    os._exit(0)
#################################################################################  Close
run = os.system
#################################################################################  Start

color = '\x1b[38;5;45m'
color2 = '\x1b[38;5;206m'
color3 = '\x1b[38;5;51m'
gray = '\x1b[38;5;206m'
reset = '\x1b[0m'
morado = '\x1b[38;5;56m'
rojo = '\x1b[38;5;196m'
cyan = '\x1b[38;5;51m'
azul = '\x1b[38;5;21m'
gris = '\033[90m'
#################################################################################  Definicion del Color

clear()
print(f'''
\x1b[38;2;0;255;255m[ \x1b[38;2;233;233;233mInstalador \x1b[38;2;0;255;255m] | \x1b[38;2;233;233;233mCloud Destroyer \x1b[38;2;0;255;255m | \x1b[38;2;0;255;255m[ \x1b[38;2;233;233;233mOnly Linux \x1b[38;2;0;255;255m]


  
                  {gris},--.    ,--.
                 (({Fore.GREEN}O {gris}))--(({Fore.GREEN}O {gris}))
               {gris},'_`--'____`--'_`.                       ##############################################
              _:  ____________  :_                      ##                                          ##    
             | | ||::::::::::|| | |                     ##         {cyan}Ready for Installation?          {gris}##       
             | | ||::::::::::|| | |                     ##                                          ##      
             | | ||::::::::::|| | |                     ##############################################
             |_| |/__________\| |_|
               |________________|
            __..-'            `-..__
         .-| : .----------------. : |-.
       ,\ || | |\______________/| | || /._
      /`.\:| | ||  __  __  __  || | |;/,' |
     :`-._\;.| || '--''--''--' || |,:/_.-':
     |    :  | || .----------. || |  :    |
     |    |  | || '----SSt---' || |  |    |
     |    |  | ||   _   _   _  || |  |    |
     :,--.;  | ||  (_) (_) (_) || |  :,--.;
     (`-'|)  | ||______________|| |  (|`-')
      `--'   | |/______________\| |   `--'
             |____________________|
              `.________________,'
               (_______)(_______)
               (_______)(_______)
               (_______)(_______)
               (_______)(_______)
              |        ||        |
              '--------''--------'┘

''')



inst = input(f"{cyan}Estas Seguro ? {color2}(Y - N):{Fore.GREEN} ")

if inst == 'Y':
    print(f'{color}> {reset}{color}[{Fore.GREEN}Cloud{Fore.LIGHTMAGENTA_EX}@{Fore.GREEN}System{color}]{gray}: Instalando speedtest-cli{Fore.GREEN} ') 
    time.sleep(2)
    run("pip3 install speedtest-cli")
    print(f'{color}> {reset}{color}[{Fore.GREEN}Cloud{Fore.LIGHTMAGENTA_EX}@{Fore.GREEN}System{color}]{gray}: Instalando PySocks{Fore.GREEN} ') 
    time.sleep(2)
    run("pip3 install PySocks")
    print(f'{color}> {reset}{color}[{Fore.GREEN}Cloud{Fore.LIGHTMAGENTA_EX}@{Fore.GREEN}System{color}]{gray}: Instalando cfscrape{Fore.GREEN} ') 
    time.sleep(2)
    run("pip3 install cfscrape")
    print(f'{color}> {reset}{color}[{Fore.GREEN}Cloud{Fore.LIGHTMAGENTA_EX}@{Fore.GREEN}System{color}]{gray}: Instalando datetime{Fore.GREEN} ') 
    time.sleep(2)
    run("pip3 install datetime")
    print(f'{color}> {reset}{color}[{Fore.GREEN}Cloud{Fore.LIGHTMAGENTA_EX}@{Fore.GREEN}System{color}]{gray}: Instalando ssl{Fore.GREEN} ') 
    time.sleep(2)
    run("pip3 install ssl")
    print(f'{color}> {reset}{color}[{Fore.GREEN}Cloud{Fore.LIGHTMAGENTA_EX}@{Fore.GREEN}System{color}]{gray}: Instalando threading{Fore.GREEN} ') 
    time.sleep(2)
    run("pip3 install threading")
    print(f'{color}> {reset}{color}[{Fore.GREEN}Cloud{Fore.LIGHTMAGENTA_EX}@{Fore.GREEN}System{color}]{gray}: Instalando icmplib{Fore.GREEN} ') 
    time.sleep(2)
    run("pip3 install imcplib")
    print(f'{color}> {reset}{color}[{Fore.GREEN}Cloud{Fore.LIGHTMAGENTA_EX}@{Fore.GREEN}System{color}]{gray}: Instalando scapy{Fore.GREEN} ') 
    time.sleep(2)
    run("pip3 install scapy")
    print(f'{color}> {reset}{color}[{Fore.GREEN}Cloud{Fore.LIGHTMAGENTA_EX}@{Fore.GREEN}System{color}]{gray}: Instalando nodejs{Fore.GREEN} ') 
    time.sleep(2)
    run("sudo apt-get install nodejs")
    print(f'{color}> {reset}{color}[{Fore.GREEN}Cloud{Fore.LIGHTMAGENTA_EX}@{Fore.GREEN}System{color}]{gray}: Instalando npm{Fore.GREEN} ') 
    time.sleep(2)
    run("sudo apt-get install npm")
    print(f'{color}> {reset}{color}[{Fore.GREEN}Cloud{Fore.LIGHTMAGENTA_EX}@{Fore.GREEN}System{color}]{gray}: Instalando Complementos npm{Fore.GREEN} ') 
    time.sleep(2)
    run("npm i events")
    run("npm i fs")
    run("npm i url")
    run("npm i net")
    run("npm i cloudscraper")
    run("npm i request")
    run("npm i randomstring")
    run("npm i cluster")
    run("npm i cloudflare-bypasser")
    run("npm i hcaptcha-solver")
    print(f'{color}> {reset}{color}[{Fore.GREEN}Cloud{Fore.LIGHTMAGENTA_EX}@{Fore.GREEN}System{color}]{gray}: Adaptando Servidor{Fore.GREEN} ') 
    time.sleep(2)
    run("ulimit -n 999999")
    run("chmod +x *")
    print(f'{color}> {reset}{color}[{Fore.GREEN}Cloud{Fore.LIGHTMAGENTA_EX}@{Fore.GREEN}System{color}]{gray}: EJECUTANDO CNC{Fore.GREEN} ') 
    time.sleep(4)
    run("python3 .\cnc.py")
elif inst == 'N':
    close()

else:
    print(f"{rojo}Tienes Que Decidir Una ? {color2}")
