print('''

  ___       _                                _     
 / _ \  ___| |_ ___  ___  ___  __ _ _ __ ___| |__  
| | | |/ __| __/ _ \/ __|/ _ \/ _` | '__/ __| '_ \ 
| |_| | (__| || (_) \__ \  __/ (_| | | | (__| | | |
 \___/ \___|\__\___/|___/\___|\__,_|_|  \___|_| |_|
                                                   
         |----------------------------------|
         |-search hide directory web tool---|
         |-----------by Octopus-------------|
         |----------------------------------|


''')
# import the library and insert the values 

import sys
import requests
import threading as th

url = sys.argv[1]
wordlist = sys.argv[2]

# import the code of other files 

# this file is use for check the connection of the website 
import octocheckwebsite as control
control.check(url)

# this file is use for enumerate the website 
import octoenumeration as enumeration
enumeration.octoenumeration(url,wordlist)
