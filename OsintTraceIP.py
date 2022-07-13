import requests
import webbrowser

#Color
grey   = "\033[1;37m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
cyan= "\033[0;96m"
purple="\033[0;35m"

def osinttraceip():
    ipinfo={}
    ip=input(red+"Ip address >> ")
    url="http://ip-api.com/json/"+ip
    r=requests.get(url)
    ipinfo=r.json()
    if ipinfo['status'] == 'success':
        lat=ipinfo['lat']
        lon=ipinfo['lon']        
        print(green+"Ip location Found !!!")
        print('\n')
        print('[+] Country     : ',ipinfo['country'])
        print('[+] Region Name : ',ipinfo['regionName'])
        print('[+] City        : ',ipinfo['city'])
        print('[+] Time zone   : ',ipinfo['timezone'])
        print('[+] ISP         : ',ipinfo['isp'])
        print(cyan+'Opening Location in browser')
        mapurl = "https://maps.google.com/maps?q=%s,+%s" % (lat, lon)
        webbrowser.open(mapurl, new=2) 
        print('')
    else:
        print(red+"Ip location Not Found !!")
        
    
        
if __name__=="__main__":
   osinttraceip()