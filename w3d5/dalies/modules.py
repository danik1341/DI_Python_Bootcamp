import requests
import time


def get_page_load_time(url):
    try:
        start_time = time.time()
        response = requests.get(url)
        response_time = time.time() - start_time
        if response.status_code == 200:
            return response_time
        else:
            return None
    except requests.exceptions.RequestException:
        return None


# Test the function with multiple sites
sites = ["https://www.google.com", "https://www.ynet.co.il",
         "https://www.imdb.com", "https://tech-store-kohl.vercel.app/"]
for site in sites:
    load_time = get_page_load_time(site)
    if load_time is not None:
        print(f"{site} loaded in {load_time:.2f} seconds.")
    else:
        print(f"Failed to load {site}.")
