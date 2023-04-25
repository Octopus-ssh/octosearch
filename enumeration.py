# import the library
import requests
import concurrent.futures

def check_url(url, path):
    # make the request
    request = requests.head(f"{url}/{path}")
    # check the status request 
    if request.status_code == 200:
        print(f"[+] {request.status_code} ---> {url}/{path}")

def enumeration(url, wordlist):
    # enumeration 
    print("[+] enumeration is starting...\n\n")
    # open the file and start threading
    with open(wordlist, "r") as file:
        paths = (line.strip() for line in file)
        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            for path in paths:
                executor.submit(check_url, url, path)
