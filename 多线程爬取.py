from concurrent.futures import ThreadPoolExecutor
from txtget import *
import time
import random
import requests

session = requests.Session()

def crawl_url(link):
    try:
        time.sleep(random.uniform(0.5,2.0))

        crawl(link)
    except requests.exceptions.RequestException as e:
        print(e)

with ThreadPoolExecutor(max_workers=10) as executor:
    executor.submit(crawl_url,'https://huananxs.com')