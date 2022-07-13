# Web domain info

import os

#Color
grey   = "\033[1;37m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
cyan= "\033[0;96m"
purple="\033[0;35m"

def webdomaininfo():
    domain = input(cyan+"Domain >> ")
    print(os.system("whois " + domain))

if __name__=="__main__":
    webdomaininfo()