# import diffrent library  
import requests
from multiprocessing.pool import ThreadPool

def check_url(url, path):
    # give the reuqest and check the itself 
    request = requests.head(f"{url}/{path}")
    if request.status_code == 200:
        print(f"[+] {request.status_code} ---> {url}/{path}")

def enumeration(url, wordlist):
    print("[+] enumeration is starting...\n\n")

    # starting the enumeration and thread
    with open(wordlist, "r") as file:
        paths = (line.strip() for line in file)

        with ThreadPool() as pool:
            pool.starmap(check_url, [(url, path) for path in paths])
