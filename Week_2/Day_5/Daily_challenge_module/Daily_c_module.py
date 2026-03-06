#
#==============================
# Daily Challenge: Modules
#==============================
#Instructions :
# Using the requests and time modules, create a function which returns the amount of time it takes a webpage to load (how long it takes for a complete response to a request).
# Test your code with multiple sites such as google, ynet, imdb, etc.



import requests
import time

def get_load_time(url):
    """
    Measures the time it takes to get a response from a URL.
    """
    try:
        start_time = time.time()
        
        response = requests.get(url)
        
        end_time = time.time()
        
        duration = end_time - start_time
        
        response.raise_for_status()
        
        return round(duration, 4)
    
    except requests.exceptions.RequestException as e:
        return f"Error connecting to {url}: {e}"

sites = [
    "https://www.google.com",
    "https://www.ynet.co.il",
    "https://www.imdb.com",
    "https://www.github.com"
]

print("Webpage Load Times (seconds):")
print("-" * 30)

for site in sites:
    result = get_load_time(site)
    print(f"{site:25} : {result}")