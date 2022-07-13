#Nmap NSE

import os

#Color
grey   = "\033[1;37m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
cyan= "\033[0;96m"
purple="\033[0;35m"


def nmapnse():
    IP = input(cyan+"IP >> ")
    print(os.system("nmap --script=vuln "+ IP ))

if __name__=="__main__":
    nmapnse()