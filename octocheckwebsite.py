def check (url) :
    import requests
    import time 
    response = requests.get(url)
    if(response.status_code == 200) : 
        c = 0 
    else :
        print(f"[-] the connection has not been established")
        return 0
        


    
