from sentiment_pipeline import SentimentPipeline
from plot_sentiments import plot_sentiments_combined
import os

def read_urls_from_file(file_name):
    product_urls = {}
    with open(file_name, 'r') as file:
        current_product = None
        for line in file:
            line = line.strip()
            if line.startswith('#'):
                current_product = line[1:].strip()
                product_urls[current_product] = []
            elif line and current_product:
                product_urls[current_product].append(line)
    return product_urls

if __name__ == "__main__":
    # Read URLs from input file
    product_urls = read_urls_from_file('input.txt')

    # Ensure output directory exists
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Run pipeline
    pipeline = SentimentPipeline(product_urls)
    sentiment_results = pipeline.process_reviews(output_dir=output_dir)

    # Plot combined results
    plot_sentiments_combined(sentiment_results)

    print("Pipeline execution completed. Check 'output/' for results.")
