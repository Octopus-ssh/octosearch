# this is the introduction to the tool

print('''

          ___       _                                _     
         / _ \  ___| |_ ___  ___  ___  __ _ _ __ ___| |__  
        | | | |/ __| __/ _ \/ __|/ _ \/ _` | '__/ __| '_ \ 
        | |_| | (__| || (_) \__ \  __/ (_| | | | (__| | | |
         \___/ \___|\__\___/|___/\___|\__,_|_|  \___|_| |_|
                      
        |-------------------------------------------------|
        | tool made by octopus to search for hidden pages |                              
        |-------------------------------------------------|


''')

# import the library
import requests
import sys
from take_data import take_data
from enumeration import enumeration


# here start main.... 

# take the url and wordlist
url,wordlist = take_data()


# start enumeration
enumeration(url,wordlist)


# end 

print("\n\n[+] thanks for using my tool :))\n")
