# Web sub domain enum

import os

#Color
grey = "\033[1;37m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
cyan = "\033[0;96m"
purple = "\033[0;35m"

def websubdomainenum():
    domain = input(cyan+"Domain >> ")
    print(os.system("sudo assetfinder -subs-only " + domain))

if __name__=="__main__":
    websubdomainenum()