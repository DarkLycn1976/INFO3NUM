#Nmap Live Host

import os

#Color
grey    =    "\033[1;37m"
red     =   "\033[1;31m"
green   =   "\033[1;32m"
yellow  =   "\033[1;33m"
cyan    =   "\033[0;96m"
purple  =   "\033[0;35m"


def livehost():
    IP = input(cyan+"IP/CIDR >> ")
    print(os.system("nmap -sP " + IP + " | grep -o 192.168.*.*"))


if __name__=="__main__":
    livehost()