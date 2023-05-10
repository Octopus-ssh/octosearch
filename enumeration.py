import requests
import concurrent.futures

def check_url(url, path):
    try:
        # Make a HEAD request to the specified URL and path
        response = requests.head(f"{url}/{path}", timeout=0.5, allow_redirects=False)
        # Check if the response status code is 200 OK
        if response.status_code == 200:
            # Print a message indicating a successful request
            print(f"[+] {response.status_code} ---> {url}/{path}")
    except (requests.exceptions.RequestException, requests.exceptions.Timeout):
        # Ignore any exceptions raised by the request
        pass

def enumeration(url, wordlist):
    # Print a message indicating the start of the directory enumeration
    print("[+] enumeration is starting...\n\n")
    with open(wordlist, "r") as file:
        # Create a generator that yields each line of the file, stripping any leading or trailing whitespace
        paths = (line.strip() for line in file)
        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            # Submit a task to the executor for each path in the wordlist
            futures = {executor.submit(check_url, url, path): path for path in paths}
            # Process the tasks as they complete
            for future in concurrent.futures.as_completed(futures):
                # Get the path associated with the completed task
                path = futures[future]
                # Ignore any exceptions raised by the task
                if future.exception() is not None:
                    continue
