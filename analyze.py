
# Azure's Text Analytics API 

import requests
import json
import os

# Import the Azure Text Analytics API client library
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Set up the Azure Text Analytics API client
subscription_key = os.environ.get("AZURE_SUBSCRIPTION_KEY")
endpoint = os.environ.get("AZURE_ENDPOINT")
credential = AzureKeyCredential(subscription_key)
client = TextAnalyticsClient(endpoint=endpoint, credential=credential)

# Define the function to extract, classify, and analyze the text
def analyze_website(url):
    # Make a GET request to the website's URL
    response = requests.get(url)
    text = response.text
    documents = [{"id": "1", "text": text}]

    # Extract the key phrases from the text
    key_phrases = client.extract_key_phrases(documents=documents)
    key_phrases = key_phrases[0].key_phrases

    # Perform sentiment analysis on the text
    sentiment = client.analyze_sentiment(documents=documents)
    sentiment = sentiment[0].sentiment

    # Perform named entity recognition on the text
    entities = client.recognize_entities(documents=documents)
    entities = entities[0].entities

    # Return the results as a dictionary
    result = {
        "key_phrases": key_phrases,
        "sentiment": sentiment,
        "entities": entities
    }
    return result

# Example usage
url = "https://www.example.com"
result = analyze_website(url)
print(result)
