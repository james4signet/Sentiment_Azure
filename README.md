# Sentiment_Azure
Using Azure Cloud for Sentiment Analysis

## Description

This project utilizes Azure's Text Analytics API to extract and analyze text from a website's URL. The user inputs a website's URL into an HTML form, and the JavaScript file sends a POST request to a Flask server that runs a Python script. The Python script uses the Azure Text Analytics API to extract key phrases, classify entities, and analyze sentiment from the website's text. The Flask server then returns the results as a JSON object, which the JavaScript file displays on the web page in a table format. The user can also enhance the visual representation of the report by using an accompanying CSS file. The project is hosted on a cloud service such as Azure or Google Cloud. The project could be used by businesses and organizations to gain insight into the content of a website and its sentiment.


## Instructions to use this project

1. Create a new Azure account: Go to https://azure.com and sign up for a new Azure account.
1. Create a new Text Analytics resource: After you've logged in, go to the Azure portal and create a new Text Analytics resource. This will allow you to access the Text Analytics API.
1. Get your endpoint and subscription key: Once the resource is created, navigate to the resource and go to "Keys and Endpoint" to get the endpoint and subscription key. You'll need these to call the API in your Python script.
1. Create a new Web App: Create a new Web App on Azure, this will allow you to host your web application on Azure.
* Go to the Azure portal and click on the "Create a resource" button.
* In the search bar, type in "Web App" and select it from the results.
* In the "Web App" page, fill in the required fields such as the subscription, resource group, name, operating system and runtime stack.
* Under the "Publish" section, select "Code" and choose the desired language runtime.
* Under the "Operating system" section, select "Windows" or "Linux" depending on your choice of runtime stack.
* Under the "Runtime stack" section, select the desired runtime stack (e.g. Python, Node.js)
* Under the "Application settings" section, you can configure your application settings if needed.

1. Click on "Review + create" then "Create" to create the web app.
1. Deploy your code: Deploy your code to the Web App, you can use Git or FTP to do that.
1. Setup your environment variables: Go to the Web App settings and set the endpoint and subscription key as environment variables.
1. Install the necessary dependencies: Make sure that the necessary dependencies are installed on the server, such as Flask and azure-ai-textanalytics.
1. Test your application: Test your application by visiting the URL of your Web App in a browser.
1. Monitor your application: Go to the Azure portal and monitor your application's performance, you can also use Azure Monitor to track and diagnose issues.

---

## Requirements

To run the project you will need the following files:

1. Python script that contains the code to extract and analyze the website's text using Azure Text Analytics API.
1. Flask file that creates a web server and maps URLs to specific functions in the Python script.
1. JavaScript file that contains the code to handle the form submission, send the HTTP requests, and display the results on the web page.
1. HTML file that defines the structure of the web page and includes the JavaScript file.
1. CSS file that contains the styling rules for the web page, this file is optional but it will make the report more user friendly.
1. You'll also need to set up an Azure account and create a Text Analytics resource and get the endpoint and subscription key, you will also need to 1. install the azure-ai-textanalytics library via pip by running pip install azure-ai-textanalytics

> Additionally, you'll need to set up a web server to host the HTML, JavaScript, and CSS files and run the Flask file. You can use a cloud service such as Google Cloud or Azure to host the web server.
