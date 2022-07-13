# NumberInfo
import requests

#color
grey   = "\033[1;37m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
cyan= "\033[0;96m"
purple="\033[0;35m"

def osintnumberinfo():
    phonenum = input(red +"Enter Mobile Number with country code >> ")
    url = ("http://apilayer.net/api/validate?access_key=cd3af5f7d1897dc1707c47d05c3759fd&number="+phonenum)
    resp = requests.get(url)
    details = resp.json()
    print('')
    print(cyan+"[+] Target                      : "+ details['number'])
    print(cyan+"[+] Target Local Format         : "+ details['local_format'])
    print(cyan+"[+] Target International Format : "+ details['international_format'])
    print(cyan+"[+] Prefix                      : "+ details['country_prefix'])
    print(cyan+"[+] Carrier                     : "+ details['carrier'])
    print(cyan+"[+] Code                        : "+ details['country_code'])
    print(cyan+"[+] Location                    : "+ details['location'])
    print(cyan+"[+] Country                     : "+ details['country_name'])
    
if __name__=="__main__":
    osintnumberinfo()
