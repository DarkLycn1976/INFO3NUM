#Hydra Web Enum
import os

#Color
grey   = "\033[1;37m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
cyan= "\033[0;96m"
purple="\033[0;35m"


def webdirenum():
    domain = input(cyan+"Domain >> ")
    print(os.system("sudo gobuster dir -e -u " + domain + " -w /usr/share/wordlists/dirb/big.txt -t 40 -q"))

if __name__=="__main__":
    webdirenum()