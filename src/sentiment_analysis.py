from openai import OpenAI

client = OpenAI(api_key='#YOUR_OPEN_API_KEY')
from transformers import pipeline

def analyze_sentiment(transcript):
    print("Analyzing Sentiment with OpenAI")
    response = client.chat.completions.create(model="gpt-4",
    messages=[
        {"role": "system", "content": "Analyze the sentiment of the following text."},
        {"role": "user", "content": transcript}
    ])

    sentiment_analysis = response.choices[0].message.content
    print("Analysed Sentiments... Returning the data")
    return sentiment_analysis

def analyze_sentiment_with_hugging_face(transcript):
    print("Analyzing Sentiments with Hugging face")
    sentiment_analyzer = pipeline("sentiment-analysis")
    results = sentiment_analyzer(transcript)
    print("Analysed Sentiments... Returning the data")
    return results  # Returns a list of dictionaries with 'label' and 'score'
