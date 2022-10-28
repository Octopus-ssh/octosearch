def check (url) :
    import requests
    import time 
    print("[+] starting the check connection of the website !")
    time.sleep(3)
    response = requests.get(url)
    if(response.status_code == 200) :
        print("\n[+] the connection of website is good !") 
    else :
        print("\n[-] the connection of website is bad ")


    
