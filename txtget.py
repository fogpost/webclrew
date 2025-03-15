import re

import requests
from bs4 import BeautifulSoup

base_url = "https://www.huananxs.cc"
start_url = "/huananxs/info/682"

pattern = re.compile(r"/huananxs/682/\d+(_\d+)?\.html$")
visited_links = set()


visited = set()
def crawl(url):

    full_url = base_url + url
    if full_url in visited_links:
        return

    print(f"正在爬取：{full_url}")
    visited_links.add(full_url)

    try:
        response = requests.get(full_url, timeout=10)
        if response.status_code != 200:
            print(f"访问失败：{full_url}(状态码: {response.status_code})")
    except requests.exceptions.RequestException as e:
        print(e)
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    links = [a["href"] for a in soup.find_all('a', href=True)]
    for link in links:
        if link.startswith("/"):
            link = link.strip()
            if pattern.match(link):
                crawl(link)

crawl(start_url)
