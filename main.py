from scraper import Scraper

URL = "https://quotes.toscrape.com/"

if __name__ == '__main__':
    scraper = Scraper(URL, headless=False)
    scraper.run()
