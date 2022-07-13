#Nmap Service Detection

import os

#Color
grey   = "\033[1;37m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
cyan= "\033[0;96m"
purple="\033[0;35m"



def nmapportserv():
    IP = input(cyan+"IP >> ")
    print(os.system("nmap -sV -Pn --min-rate 300 " + IP))

if __name__=="__main__":
    nmapportserv()



