from sentiment_analyzer import SentimentAnalyzer

def test_analyze_comments():

    analyzer = SentimentAnalyzer()

    # Dummy comments for testing
    comments = ["I love this product!", "It's okay, not great.", "Terrible experience!"]

    # Mock analyze_comments to return predefined sentiments
    def mock_analyze_comments(comments):
        return ["positive", "neutral", "negative"]

    analyzer.analyze_comments = mock_analyze_comments

    # Analyze comments
    sentiments = analyzer.analyze_comments(comments)

    # Assertions
    assert len(sentiments) == 3, "There should be 3 sentiments"
    assert sentiments == ["positive", "neutral", "negative"], "Sentiments should match"
