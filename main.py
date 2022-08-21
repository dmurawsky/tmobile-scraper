"""Application entry point."""
from scraper import scrape_page
from config import URL

if __name__ == '__main__':
    scrape_page(URL)
