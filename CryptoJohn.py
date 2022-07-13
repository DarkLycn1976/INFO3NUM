#john the ripper
import os

#Color
grey   = "\033[1;37m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
cyan= "\033[0;96m"
purple="\033[0;35m"


def cryptojohn():

    hash = input(cyan+"HASH >> ")
    htype = input(cyan+"HASH TYPE>> ")
    print(os.system(' echo '+ hash +' >> hash.txt'))
    print(os.system("sudo john --format="+ htype +" --wordlist=rockyou.txt hash.txt"))
    


if __name__=="__main__":
    cryptojohn()
