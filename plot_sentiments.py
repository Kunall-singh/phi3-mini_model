import matplotlib.pyplot as plt
import numpy as np

def plot_sentiments_combined(sentiment_results):
    # Define colors for the sentiments
    colors = {'negative': 'red', 'positive': 'blue', 'neutral': 'yellow'}
    devices = list(sentiment_results.keys())
    sentiments = ['negative', 'positive', 'neutral']
    
    # Prepare data for plotting
    counts = {sentiment: [0] * len(devices) for sentiment in sentiments}
    for i, device in enumerate(devices):
        sentiment_counts = {'negative': 0, 'positive': 0, 'neutral': 0}
        for sentiment in sentiment_results[device]:
            sentiment_counts[sentiment] += 1
        
        for sentiment in sentiments:
            counts[sentiment][i] = sentiment_counts[sentiment]
    
    # Bar width and positions
    bar_width = 0.2
    x = np.arange(len(devices))
    
    # Plot each sentiment type
    for i, sentiment in enumerate(sentiments):
        plt.bar(
            x + i * bar_width, 
            counts[sentiment], 
            bar_width, 
            label=sentiment.capitalize(), 
            color=colors[sentiment]
        )
    
    # Add labels, title, and legend
    plt.xlabel('Devices')
    plt.ylabel('Sentiment Counts')
    plt.title('Sentiment Analysis for All Devices')
    plt.xticks(x + bar_width, devices, rotation=45, ha='right')
    plt.legend(title='Sentiments')
    
    # Save and display the plot
    plt.tight_layout()
    plt.savefig('output/sentiment_analysis_combined_plot.png')
    plt.show()
