# Sentiment_Azure
Using Azure Cloud for Sentiment Analysis

## Description

This project utilizes Azure's Text Analytics API to extract and analyze text from a website's URL. The user inputs a website's URL into an HTML form, and the JavaScript file sends a POST request to a Flask server that runs a Python script. The Python script uses the Azure Text Analytics API to extract key phrases, classify entities, and analyze sentiment from the website's text. The Flask server then returns the results as a JSON object, which the JavaScript file displays on the web page in a table format. The user can also enhance the visual representation of the report by using an accompanying CSS file. The project is hosted on a cloud service such as Azure or Google Cloud. The project could be used by businesses and organizations to gain insight into the content of a website and its sentiment.


## Requirements

To run the project you will need the following files:

1. Python script that contains the code to extract and analyze the website's text using Azure Text Analytics API.
1. Flask file that creates a web server and maps URLs to specific functions in the Python script.
1. JavaScript file that contains the code to handle the form submission, send the HTTP requests, and display the results on the web page.
1. HTML file that defines the structure of the web page and includes the JavaScript file.
1. CSS file that contains the styling rules for the web page, this file is optional but it will make the report more user friendly.
1. You'll also need to set up an Azure account and create a Text Analytics resource and get the endpoint and subscription key, you will also need to 1. install the azure-ai-textanalytics library via pip by running pip install azure-ai-textanalytics

> Additionally, you'll need to set up a web server to host the HTML, JavaScript, and CSS files and run the Flask file. You can use a cloud service such as Google Cloud or Azure to host the web server.
