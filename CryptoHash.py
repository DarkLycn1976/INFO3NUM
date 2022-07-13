
from CryptoHashIdentityfier import cryptohashid
from CryptoHashcat import cryptohashcat
from CryptoJohn import cryptojohn

#Color
grey    = "\033[1;37m"
red     = "\033[1;31m"
green   = "\033[1;32m"
yellow  = "\033[1;33m"
cyan    = "\033[1;96m"
purple  = "\033[1;35m"


def cryptohash():
    from Info3num import main_menu
    print(yellow + """
                                    Available Scripts 

                                <a> Hash Identifier
                                <b> Hash Cracking - <John The Ripper>
                                <c> Hash Cracking - <HashCat>

    """)

    inp = (input(cyan + "Choose >> "))
    if (inp == 'a'):
        cryptohashid()
    elif (inp == 'b'):
        cryptojohn()
    elif (inp == 'c'):
        cryptohashcat()
    elif (inp == 'back'):
        main_menu()

    elif (inp == 'exit'):
        exit()
    elif (inp == 'x'):
        print(red + "Hint :")
        print(green + "ls " + grey + "  - to list scripts.")
        print(green + "back " + grey + "  - previous modules.")
        print(green + "exit " + grey + "- to exit the tool.")
    elif (inp == 'ls'):
        print(green + """
                                    Tools available 

                                <a> Hash Identifier
                                <b> Hash Cracking - <John The Ripper>
                                <c> Hash Cracking - <HashCat>

            """)
    else:
        print(red + "Enter an valid option")
    while True:
        cryptohash()


if __name__ == "__main__":
    cryptohash()

