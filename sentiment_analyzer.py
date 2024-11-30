import subprocess
class SentimentAnalyzer:
    def __init__(self, model_name='phi3'):
        self.model_name = model_name
        self.valid_sentiments = {'positive', 'negative', 'neutral'}

    def analyze_sentiment(self, comment):
        prompt = f"Based on the following comment: '{comment}', respond with one word only: positive, negative, or neutral."
        process = subprocess.run(
            ['ollama', 'run', self.model_name, prompt],
            capture_output=True, text=True, check=True
        )
        response = process.stdout.strip()
    
        # Debug: Log the raw response from the model
        print(f"DEBUG: Comment: {comment}\nModel Response: {response}\n")
    
        # Extract sentiment
        sentiment = response.split()[-1].strip('.').lower()
        return sentiment if sentiment in self.valid_sentiments else "neutral"


    def analyze_comments(self, comments):
        return [self.analyze_sentiment(comment) for comment in comments]
