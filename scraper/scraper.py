# Author: Kunal Singh
# This script scrapes product reviews for different Samsung Galaxy versions from eBay and saves them into text files.

import requests
from bs4 import BeautifulSoup

# Function to read URLs from the text file
def read_urls_from_file(file_name):
    product_urls = {}
    with open(file_name, 'r') as file:
        current_product = None
        for line in file:
            line = line.strip()
            if line.startswith('#'):  # Lines starting with '#' are product version names
                current_product = line[1:].strip()
                product_urls[current_product] = []
            elif line and current_product:  # URLs are stored under the respective product
                product_urls[current_product].append(line)
    return product_urls

# Function to scrape reviews from a single page
def scrape_reviews(url):
    response = requests.get(url)                        # Sending a request to the URL to retrieve the page content
    if response.status_code != 200:  
        print(f"Failed to retrieve {url}. Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')  # Parsing the HTML content using BeautifulSoup

    # Find all sections containing reviews
    review_sections = soup.find_all('div', class_='ebay-review-section')

    if not review_sections:
        print(f"No reviews found on the page: {url}")
        return []

    # Extract and return the text content of the reviews
    return [section.find('p').text.strip() for section in review_sections if section.find('p')]

# Function to save reviews to a file
def save_reviews(version, reviews):
    filename = f'{version}_reviews.txt'
    with open(filename, 'a') as file:  # 'a' mode to append to the file if it already exists
        for i, review in enumerate(reviews, 1):
            file.write(f"Review {i}:\n{review}\n\n")
    print(f"Saved {len(reviews)} reviews to {filename}")

# Main execution: read URLs from the file and scrape reviews
if __name__ == "__main__":
    product_urls = read_urls_from_file('input.txt')  # Read URLs from the text file

    for version, urls in product_urls.items():
        all_reviews = []
        print(f"Scraping reviews for {version}")
        
        for url in urls:
            print(f"Scraping URL: {url}")
            reviews = scrape_reviews(url)
            all_reviews.extend(reviews)  # Collect reviews from all pages for the product
        
        save_reviews(version, all_reviews)  # Save all collected reviews for this product version
        print(f"Total reviews scraped for {version}: {len(all_reviews)}\n")
