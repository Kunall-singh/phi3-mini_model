from plot_sentiments import plot_sentiments_combined

def test_plot_sentiments_combined(tmpdir):

    # Dummy sentiment results
    sentiment_results = {
        "Samsung_Galaxy_S20": ["positive", "negative", "neutral"],
        "Samsung_Galaxy_S21": ["positive", "positive", "neutral"]
    }

    # Generate plot
    plot_sentiments_combined(sentiment_results)

    # Validate the file was created
    plot_file = "output/sentiment_analysis_combined_plot.png"
    assert plot_file, "Plot file should exist."
