from WebDomainInfo import webdomaininfo
from WebDirEnum import webdirenum
from WebSubdomainEnum import websubdomainenum


# Color

#Color
grey    = "\033[1;37m"
red     = "\033[1;31m"
green   = "\033[1;32m"
yellow  = "\033[1;33m"
cyan    = "\033[1;96m"
purple  = "\033[1;35m"

def webenum():
    from Info3num import main_menu
    print(yellow + """
                                    Available Scripts 

                                <a> Web Domain Information
                                <b> Web Directory Enumeration
                                <c> Web Subdomain Enumeration 
                    

    """)
    inp = (input(cyan + "Choose >> "))
    if (inp == 'a'):
        webdomaininfo()
    elif (inp == 'b'):
        webdirenum()
    elif (inp == 'c'):
        websubdomainenum()
    elif (inp == "back"):
        main_menu()
    elif (inp == 'exit'):
        exit()


    elif (inp == 'ls'):
        print(green + """
                                    Available Scripts 

 
                                <a> Web Domain Information
                                <b> Web Directory Enumeration
                                <c> Web Subdomain Enumeration 


            """)
    elif (inp == 'x'):
        print(red + "Hint :")
        print(green + "ls " + grey + "  - to list scripts.")
        print(green + "back " + grey + "  - previous modules.")
        print(green + "exit " + grey + "- to exit the tool.")
    else:
        print(red + "Enter an valid option")
    while True:
        webenum()


if __name__ == "__main__":
    webenum()

