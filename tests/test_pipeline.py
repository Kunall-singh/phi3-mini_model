from sentiment_pipeline import SentimentPipeline

def test_process_reviews(tmpdir):

    # Dummy product URLs and mock data
    product_urls = {"Samsung_Galaxy_S20": ["https://example.com"]}
    pipeline = SentimentPipeline(product_urls)

    # Mock fetch_reviews and analyze_comments
    def mock_fetch_reviews():
        return {"Samsung_Galaxy_S20": ["Great product!", "Not good."]}

    def mock_analyze_comments(comments):
        return ["positive", "negative"]

    pipeline.scraper.fetch_reviews = mock_fetch_reviews
    pipeline.analyzer.analyze_comments = mock_analyze_comments

    # Process reviews
    output_dir = tmpdir.mkdir("output")
    results = pipeline.process_reviews(output_dir=str(output_dir))

    # Assertions
    assert results["Samsung_Galaxy_S20"] == ["positive", "negative"], "Results should match"
    output_file = output_dir.join("Samsung_Galaxy_S20_sentiments.txt")
    assert output_file.isfile(), "Output file should exist"
    assert output_file.read().splitlines() == ["positive", "negative"]
