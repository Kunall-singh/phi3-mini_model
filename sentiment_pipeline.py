from review_scraper import ReviewScraper
from sentiment_analyzer import SentimentAnalyzer

class SentimentPipeline:
    def __init__(self, product_urls):
        self.scraper = ReviewScraper(product_urls)
        self.analyzer = SentimentAnalyzer()

    def process_reviews(self, output_dir='output'):
        reviews = self.scraper.fetch_reviews()
        results = {}

        for product, comments in reviews.items():
            sentiments = self.analyzer.analyze_comments(comments)
            results[product] = sentiments

            # Save sentiments to file
            output_file = f"{output_dir}/{product}_sentiments.txt"
            with open(output_file, 'w') as file:
                for sentiment in sentiments:
                    file.write(f"{sentiment}\n")

        return results
