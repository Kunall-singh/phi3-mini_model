import requests
from bs4 import BeautifulSoup

class ReviewScraper:
    def __init__(self, product_urls):
        self.product_urls = product_urls

    def scrape_reviews(self, url):
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to retrieve {url}")
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        review_sections = soup.find_all('div', class_='ebay-review-section')
        return [section.find('p').text.strip() for section in review_sections if section.find('p')]

    def fetch_reviews(self):
        all_reviews = {}
        for product, urls in self.product_urls.items():
            product_reviews = []
            for url in urls:
                product_reviews.extend(self.scrape_reviews(url))
            all_reviews[product] = product_reviews
        return all_reviews
