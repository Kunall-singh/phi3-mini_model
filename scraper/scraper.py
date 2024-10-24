# Author: Kunal Singh
# This script scrapes product reviews for different Samsung Galaxy versions from eBay and saves them into text files.

import requests                 # To send HTTP requests to fetch the web pages
from bs4 import BeautifulSoup   # To parse the HTML content of the web pages

product_urls = {
    'Samsung_Galaxy_S20': 'https://www.ebay.com/urw/Samsung-Galaxy-S20-Ultra-5G-128-GB-Black-Unlocked-/product-reviews/10041848098?pgn=1',
    'Samsung_Galaxy_S21': 'https://www.ebay.com/urw/Samsung-Galaxy-S21-Ultra-5G-512-GB-Black-Unlocked-/product-reviews/13043687483?pgn=1',
    'Samsung_Galaxy_S22': 'https://www.ebay.com/urw/Samsung-Galaxy-S22-Ultra-512-GB-Black-Unlocked-/product-reviews/13052280684?pgn=1',
    'Samsung_Galaxy_S23': 'https://www.ebay.com/urw/Samsung-Galaxy-S23-Ultra-256-GB-Black-Unlocked-/product-reviews/23059054247?pgn=1'
}

# Function to scrape reviews from a single page
def scrape_reviews(url):
    response = requests.get(url)                        # Sending a request to the URL to retrieve the page content
    if response.status_code != 200:  
        print(f"Failed to retrieve {url}. Status code: {response.status_code}")
        return [] 
    
    soup = BeautifulSoup(response.text, 'html.parser')  # Parsing the HTML content using BeautifulSoup

    # Finding all sections of the page that contain reviews (based on specific HTML structure)
    review_sections = soup.find_all('div', class_='ebay-review-section')  

    if not review_sections:  
        print(f"No reviews found on the page: {url}")
        return []

    # Extracting and returning the text content of the reviews
    return [section.find('p').text.strip() for section in review_sections if section.find('p')]

# Function to save reviews to a file, where each product version gets its own file
def save_reviews(version, reviews):
    filename = f'{version}_reviews.txt'  
    with open(filename, 'w') as file:  
        for i, review in enumerate(reviews, 1):  
            file.write(f"Review {i}:\n{review}\n\n")  # Writing each review to the file
    print(f"Saved {len(reviews)} reviews to {filename}")  

# Main execution to scrape and save reviews for each product version
if __name__ == "__main__":
    
    for version, url in product_urls.items():
        print(f"Scraping reviews for {version} from {url}")
        
        # Scrape reviews from the current URL
        reviews = scrape_reviews(url)
        
        # Save the scraped reviews into separate files based on the product version
        save_reviews(version, reviews)
        
        print(f"Total reviews scraped for {version}: {len(reviews)}\n")  # Log the total number of reviews scraped
