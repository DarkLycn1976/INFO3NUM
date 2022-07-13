
#Color
grey    = "\033[1;37m"
red     = "\033[1;31m"
green   = "\033[1;32m"
yellow  = "\033[1;33m"
cyan    = "\033[1;96m"
purple  = "\033[1;35m"


def main_menu():

    print(cyan +"""


        |+||+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|
        |+|    _________  _         _______   _______   ______    _                   _______      |+|
        |+|    \__   __/ ( (    /| (  ____ \ (  ___  ) / ___  \  ( (    /| |\     /| (       )     |+|
        |+|       ) (    |  \  ( | | (    \/ | (   ) | \/   \  \ |  \  ( | | )   ( | | () () |     |+|
        |+|       | |    |   \ | | | (__     | |   | |    ___) / |   \ | | | |   | | | || || |     |+|
        |+|       | |    | (\ \) | |  __)    | |   | |   (___ (  | (\ \) | | |   | | | |(_)| |     |+|
        |+|       | |    | | \   | | (       | |   | |       ) \ | | \   | | |   | | | |   | |     |+|
        |+|    ___) (___ | )  \  | | )       | (___) | /\___/  / | )  \  | | (___) | | )   ( |     |+|
        |+|    \_______/ |/    )_) |/        (_______) \______/  |/    )_) (_______) |/     \|     |+|
        |+|                                                                                        |+|
        |+||+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|+|    
                                                                
                                                                """)
    print("")
    print(yellow + """
                                    Available Scripts 

                                <a> Network Enumeration 
                                <b> Web Enumeration
                                <c> Open Source Intelligence (OSINT)
                                <d> Cryptography
                                <i> info
                                <x> Hint

    """)

    info3num()

def info3num():
    from NetworkEnum import networkenum
    from WebEnum import webenum
    from CryptoHash import cryptohash
    from Osint import osint

    inp = (input(cyan + "Choose >> "))
    if (inp == 'a'):
        networkenum()
    elif (inp == 'b'):
        webenum()
    elif (inp == 'c'):
        osint()
    elif (inp == 'd'):
        cryptohash()
    elif (inp == 'exit'):
        exit()
    elif (inp == 'i'):
        print(green +"""
        
            |>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>|
            |*                                                                                          *|
            |*    Created By      : Krithik Babu P                                                      *|
            |*    LinkedIn        : https://www.linkedin.com/in/krithik-babu-p-bb97431a9/               *|                                                                            
            |*    Project Name    : INFO3NUM | Infomation Enumeration Tool                              *|
            |*    Created Date    : 30.11.2021                                                          *|
            |*    Domain          : Cybersecurity                                                       *|
            |*    Use             : Used to enumerate the active host/website for Penteration Testing   *|
            |*                                                                                          *|
            |<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<|  
        
        
        """)
    elif (inp == 'x'):
        print(red + "Hint :")
        print(green + "ls " + grey + "  - to list scripts.")
        print(green + "back " + grey + "  - previous modules.")
        print(green + "exit " + grey + "- to exit the tool.")
    elif (inp == 'ls'):
        print(green + """
                                    Tools available 

                                <a> Network Enumeration 
                                <b> Web Enumeration
                                <c> Open Source Intelligence (OSINT)
                                <d> Cryptography
                                <i> info
                                <x> Hint
             
            """)
    else:
        print(red + "Enter an valid option")

    while True:
        info3num()
    


if __name__ == "__main__":
    main_menu()