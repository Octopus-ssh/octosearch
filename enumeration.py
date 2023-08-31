import requests
import concurrent.futures
from rich import print

def check_url(url, path):
    try:
        # Make a HEAD request to the specified URL and path
        response = requests.head(f"{url}/{path}", timeout=0.5, allow_redirects=False)
        # Check if the response status code is 200 or 301 OK
        if response.status_code == 200 or response.status_code == 301 :
            # Print a message indicating a successful request
            print(f"[yellow][+] {url}/{path}")
    except (requests.exceptions.RequestException, requests.exceptions.Timeout):
        # Ignore any exceptions raised by the request
        pass

# Function for enumeration
def enumeration(url, wordlist):
    print("[bold green][+] Enumeration is about to start...\n")

    # Open the wordlist file with UTF-8 encoding, ignoring errors
    with open(wordlist, "r", encoding="utf-8", errors='ignore') as file:
        # Read and strip each line in the file to get paths
        paths = (line.strip() for line in file)

        # Create a ThreadPoolExecutor with 100 maximum workers
        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            futures = []
            # Submit tasks for each path in the wordlist
            for path in paths:
                future = executor.submit(check_url, url, path)
