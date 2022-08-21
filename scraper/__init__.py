"""Scrape metadata from target URL."""
import requests
from bs4 import BeautifulSoup
from .scrape import (
    get_link_hrefs
)

memo = []

def scrape_page(url):
    """Scrape target URL for links."""
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
    r = requests.get(url, headers=headers)
    html = BeautifulSoup(r.content, 'html.parser')
    
    links = get_link_hrefs(html)

    for link in links:
        if link:
            if link in memo: continue

            memo.append(link)

            if "@" in link or ".pdf" in link: 
                continue
            elif "tmobile-familymode.com" in link:
                print(link)
            elif link[0] == "/":
                print("Scraping: " + link)
                scrape_page("https://www.t-mobile.com" + link)
            elif "t-mobile.com" in link:
                print("Scraping: " + link)
                scrape_page(link)
