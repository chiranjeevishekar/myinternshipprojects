import requests
from bs4 import BeautifulSoup
import csv

# Define the URL of the Times of India website
url = 'https://timesofindia.indiatimes.com/'

# Send an HTTP GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the webpage using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find and extract the article titles and links
    articles = soup.find_all('a', class_='w_img')

    article_data = []

    for article in articles:
        title = article.get_text()
        link = article['href']
        article_data.append({'Title': title, 'Link': link})

    # Define the name of the CSV file to save the data
    csv_filename = 'times_of_india_articles.csv'

    # Save the data in CSV format
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['Title', 'Link']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(article_data)

    print(f"Scraped data saved to {csv_filename}")

else:
    print("Failed to retrieve data from the website.")
