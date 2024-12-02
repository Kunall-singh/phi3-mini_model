from review_scraper import ReviewScraper

def test_fetch_reviews():

    # Simulated product URLs and dummy implementation
    product_urls = {
        "Samsung_Galaxy_S20": ["https://example.com/review1", "https://example.com/review2"]
    }

    scraper = ReviewScraper(product_urls)

    # Mock scrape_reviews to avoid making HTTP requests
    def mock_scrape_reviews(url):
        return [f"Review content for {url}"]

    scraper.scrape_reviews = mock_scrape_reviews

    reviews = scraper.fetch_reviews()

    # Validate the results
    assert reviews["Samsung_Galaxy_S20"] == [
        "Review content for https://example.com/review1",
        "Review content for https://example.com/review2"
    ], "Fetched reviews should match mock data."
