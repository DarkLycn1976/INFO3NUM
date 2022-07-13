from NmapComp import nmapcomp
from NmapServ import nmapportserv
from NmapLiveHost import livehost
from NmapOs import nmapos
from NmapNSE import nmapnse

#Color
grey    = "\033[1;37m"
red     = "\033[1;31m"
green   = "\033[1;32m"
yellow  = "\033[1;33m"
cyan    = "\033[1;96m"
purple  = "\033[1;35m"

def networkenum():
    from Info3num import main_menu

    print(yellow + """
                                    Available Scripts 

                                <a> Nmap Comprehensive (all)
                                <b> Nmap Service Version Detection
                                <c> Nmap OS Detection
                                <d> Nmap Live Host Detection
                                <e> Nmap Scripting Engine (NSE-ALL)
                    

    """)



    inp = (input(cyan + "Choose >> "))
    if (inp == 'a'):
        nmapcomp()
    elif (inp == 'b'):
        nmapportserv()
    elif (inp == 'c'):
        nmapos()
    elif (inp == 'd'):
        livehost()
    elif (inp == 'e'):
        nmapnse()
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

                                <a> Nmap Comprehensive (all)
                                <b> Nmap Service Version Detection
                                <c> Nmap OS Detection
                                <d> Nmap Live Host Detection
                                <e> Nmap Scripting Engine (NSE-ALL)
            
            """)
    else:
        print(red + "Enter an valid option")
    while True:
        networkenum()


if __name__ == "__main__":
    networkenum()

