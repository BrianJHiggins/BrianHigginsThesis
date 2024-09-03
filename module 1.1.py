# module 1.1 webscrape_transcripts_list
# Web scrapes list of transcripts from Seeking Alpha website endpoint URL (line 36)
# updates S&P 500 companies
# instruction to user: insert desired web page range at line 33 below
# writes list to 'transcripts_list_data.csv' and updates S&P500 companies
# requires file 'S&P 500 Index Stocks List.csv' to flag the S&P 500 companies

from bs4 import BeautifulSoup
import csv
import time
from selenium import webdriver
import json
from random import randint

# Load S&P 500 companies
sp500_companies = set()
with open('S&P 500 Index Stocks List.csv', 'r') as spfile:
    spreader = csv.DictReader(spfile)
    for row in spreader:
        sp500_companies.add(row['Symbol'])

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open the output CSV file in write mode and write the headers
with open('transcripts_list_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['id', 'company_name', 'ticker', 'text', 'date', 'S&P500_Company']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

# Loop through pages
# insert desired page range
for page_number in range(301, 303):

    # SeekingAlpha API endpoint
    url = f"https://seekingalpha.com/api/v3/articles?filter[category]=earnings%3A%3Aearnings-call-transcripts&filter[since]=0&filter[until]=0&include=author%2CprimaryTickers%2CsecondaryTickers&isMounting=true&page[size]=50&page[number]={page_number}"

    # Navigate to the URL
    driver.get(url)
    time.sleep(randint(4, 9))  # Adjust this delay as needed to ensure the page loads completely

    # Extract page content - JSON list
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'html.parser')
    json_data = json.loads(soup.body.text)

    # Extract data and append to CSV
    with open('transcripts_list_data.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        for item in json_data['data']:
            id = item['id']
            title = item['attributes']['title']
            company_name = title.split('(')[0].strip()
            ticker = title.split('(')[1].split(')')[0]
            text = title.split('(')[1].split(')')[1].strip()
            date = item['attributes']['publishOn']

            sp500_company = 'Yes' if ticker in sp500_companies else 'No'

            writer.writerow(
                {'id': id, 'company_name': company_name, 'ticker': ticker,
                 'text': text, 'date': date, 'S&P500_Company': sp500_company})

    time.sleep(randint(4, 9))

print("Data has been extracted and written to 'transcripts_list_data.csv'.")
