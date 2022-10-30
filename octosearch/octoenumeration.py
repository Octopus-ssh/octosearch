def octoenumeration (url,wordlist) :
    import time 
    import threading as th
    import requests 
    from math import modf
    url = url 
    file = open(wordlist,"r").readlines()
    print(f"\n[+] the enumeration is start !")
    count = 0 
    with open(wordlist, 'r') as fp:
        for count, line in enumerate(fp):
            pass
    print(f'\n[+] Total Lines are', count + 1)
    
    # make a values for conditional
    num_words = count 
    rest = num_words % 1000
    rest = rest + 1 
    thread_n = count / 300
    fraz = modf(thread_n)


    print(f"\n[+] thread numbers we are using are {fraz[1]}")

    #temporary values
    start =  0
    end = 0

    #insert the main values 
    main(file,url,rest,num_words,start,end)
 
#function for bruteforce 

def octobrute (file,url,start,end) :
    import requests
    i = start 
    start1 = end 
    #enumeration of html file 
    for i,line in enumerate(file) : 
        if(i > start and i < start1 ) :
            request1 = url + line + ".html"
            request1 = request1.replace("\n","")
            get1 = requests.get(request1)
            if(get1.status_code == 200 or get1.status_code == 406):
                print(f"\n[+] <{get1.status_code}> ---> {request1}")
                continue 
    #enumeration of css file 
    i = start 
    start1 = end
    for i,line in enumerate(file) :
        if(i > start and i < start1 ) :
            request2 = url + line + ".css"
            request2 = request2.replace("\n","")
            get2 = requests.get(request2)
            if(get2.status_code == 200 or get2.status_code == 406):
                print(f"\n[+] <{get2.status_code}> ---> {request2}")
                continue
    #enumeration of javascript file 
    i = start 
    start1 = end
    for i,line in enumerate(file) :
        if(i > start and i < start1 ) :
            request3 = url + line + ".js"
            request3 = request3.replace("\n","")
            get3 = requests.get(request3)
            if(get3.status_code == 200 or get3.status_code == 406):
                print(f"\n[+] <{get3.status_code}> ---> {request3}")
                continue
    #enumeration of php file 
    i = start 
    start1 = end 
    for i,line in enumerate(file) :
        if(i > start and i < start1 ) :
            request4 = url + line + ".php"
            request4 = request4.replace("\n","")
            get4 = requests.get(request4)
            if(get4.status_code == 200 or get4.status_code == 406):
                print(f"\n[+] <{get4.status_code}> ---> {request4}")
                continue
    #enumeration of json file 
    i = start 
    start1 = end 
    for i,line in enumerate(file) :
        if(i > start and i < start1 ) :
            request5 = url + line + ".json"
            request5 = request5.replace("\n","")
            get5 = requests.get(request5)
            if(get5.status_code == 200 or get5.status_code == 406):
                print(f"\n[+] <{get5.status_code}> ---> {request5}")
                continue

def main(file,url,rest,num_words,start,end) :
    import threading as th
    if(num_words > -1) :
        start = -1 
        end = 299
        th.Thread(target=octobrute,args=(file,url,start,end)).start()

    ###############################################################   
    
    if(num_words > 299) :
        start = 299
        end = 599
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
        
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()

    ###############################################################   

    if(num_words > 599) :
        start = 599
        end = 899
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    
    ###############################################################   

    if(num_words > 899) :
        start = 899
        end = 1199
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()

    ###############################################################   

    if(num_words > 1199) :
        start = 1199
        end = 1499
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()

    ###############################################################   

    if(num_words > 1499) :
        start = 1499
        end = 1799
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()

    ###############################################################   

    if(num_words > 1799) :
        start = 1799
        end = 2099
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()

    ###############################################################   

    if(num_words > 2099) :
        start = 2099
        end = 2399
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 2399) :
        start = 2399
        end = 2699
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 2699) :
        start = 2699
        end = 2999
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 2999) :
        start = 2999
        end = 3299
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 3299) :
        start = 3299
        end = 3599
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()

    ###############################################################   

    if(num_words > 3599) :
        start = 3599
        end = 3899
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()

    ###############################################################   

    if(num_words > 3899) :
        start = 3899
        end = 4199
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 4199) :
        start = 4199
        end = 4499
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 4499) :
        start = 4499
        end = 4799
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 4799) :
        start = 4799
        end = 5099
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 5099) :
        start = 5099
        end = 5399
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()

    ###############################################################   

    if(num_words > 5399) :
        start = 5399
        end = 5699
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 5699) :
        start = 5699
        end = 5999
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()

    ###############################################################   

    if(num_words > 5999) :
        start = 5999
        end = 6299
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 6299) :
        start = 6299
        end = 6599
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 6599) :
        start = 6599
        end = 6899
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 6899) :
        start = 6899
        end = 7199
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 7199) :
        start = 7199
        end = 7499
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 7499) :
        start = 7499
        end = 7799
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 7799) :
        start = 7799
        end = 8099
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 8099) :
        start = 8099
        end =  8399
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 8399) :
        start = 8399
        end = 8699
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 8699) :
        start = 8699
        end = 8999
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()

    ###############################################################   

    if(num_words > 8999) :
        start = 8999
        end = 9299
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 9299) :
        start = 9299
        end = 9599
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 9599) :
        start = 9599
        end = 9899
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 9899) :
        start = 9899
        end = 10199
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 10199) :
        start = 10199
        end = 10499
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 10499) :
        start = 10499
        end = 10.799
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 10799) :
        start = 10799
        end = 11099
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 11099) :
        start = 11099
        end = 11399
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 11399) :
        start = 11399
        end = 11699
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 11699) :
        start = 11699
        end = 11999
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 11999) :
        start = 11999
        end = 12299
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 12299) :
        start = 12299
        end = 12599
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 12599) :
        start = 12599
        end = 12899
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 12899) :
        start = 12899
        end = 13199
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 13199) :
        start = 13199
        end = 13499
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 13499) :
        start = 13499
        end = 13799
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 13799) :
        start = 13799
        end = 14099
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 14099) :
        start = 14099
        end = 14399
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 14399) :
        start = 14399
        end = 14399
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 14399) :
        start = 14399
        end = 14699
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 14699) :
        start = 14699
        end = 14999
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 14999) :
        start = 14999
        end = 15299
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 15299) :
        start = 15299
        end = 15599
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 15599) :
        start = 15599
        end = 15899
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 15899) :
        start = 15899
        end = 16199
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 16199) :
        start = 16199
        end = 16499
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 16499) :
        start = 16499
        end = 16799
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 16799) :
        start = 16799
        end = 17099
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 17099) :
        start = 17099
        end = 17399
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 17399) :
        start = 17399
        end = 17699
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 17699) :
        start = 17699
        end = 17999
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 17999) :
        start = 17999
        end = 18299
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 18299) :
        start = 18299
        end = 18599
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 18599) :
        start = 18599
        end = 18899
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 18899) :
        start = 18899
        end = 19199
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 19199) :
        start = 19199
        end = 19499
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 19499) :
        start = 19499
        end = 19799
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()
    
    ###############################################################   

    if(num_words > 19799) :
        start = 19799
        end = 20000
        th.Thread(target=octobrute,args=(file,url,start,end)).start()
    else :
        th.Thread(target=octobrute,args=(file,url,start,rest)).start()