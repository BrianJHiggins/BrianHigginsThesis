# Module_2_webscrape_transcripts
# web scrapes S&P 500 transcripts by iterating through 'transcripts_list_data.csv'
# inserts 'id' values marked as 'S&P_500' into the (endpoint) url. line 39
# writes output to file 'transcriptscraped_test_data.csv'
# Note: data is appended to the existing list if there

import csv
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from random import randint
from selenium.common.exceptions import WebDriverException

# Function to scrape text data from a single URL using BeautifulSoup
def scrape_text(driver, url):
    time.sleep(randint(4, 9))  # Random sleep between 4 and 9 seconds
    driver.get(url)
    try:
        page_content = driver.page_source
        soup = BeautifulSoup(page_content, 'html.parser')
        text_element = soup.find('body')
        if text_element:
            transcript_text = text_element.get_text()
        else:
            transcript_text = None
        return transcript_text
    except Exception as e:
        print(f"Error occurred while scraping text from URL: {url}")
        print(e)
        return None

# Function to process a batch of URLs and scrape text data
def process_batch(driver, batch, writer):
    for row in batch:
        id = row['id']
        company_name = row['company_name']
        ticker = row['ticker']
        date = row['date']
        text = row['text']

        url = f"https://seekingalpha.com/api/v3/articles/{id}?include=author%2CprimaryTickers%2CsecondaryTickers%2CotherTags%2Cpresentations%2Cpresentations.slides%2Cauthor.authorResearch%2Cauthor.userBioTags%2Cco_authors%2CpromotedService%2Csentiments"
        scraped_text = scrape_text(driver, url)

        if scraped_text:
            text_chunks = [scraped_text[i:i + 8000] for i in range(0, len(scraped_text), 8000)]
            for chunk in text_chunks:
                writer.writerow({'id': id, 'company_name': company_name, 'ticker': ticker, 'date': date, 'text': text, 'transcript_text': chunk})
        else:
            writer.writerow({'id': id, 'company_name': company_name, 'ticker': ticker, 'date': date, 'text': text, 'transcript_text': ''})

# Function to process the CSV file and scrape text data
def process_csv(input_csv, output_csv):
    # Open the WebDriver
    driver = webdriver.Chrome()

    with open(input_csv, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        with open(output_csv, 'a', newline='', encoding='utf-8') as outfile:
            fieldnames = ['id', 'company_name', 'ticker', 'date', 'text', 'transcript_text']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            batch = []
            for row in reader:
                if row['S&P500_Company'] == 'Yes':  # Check if the company is in S&P500
                    batch.append(row)
                if len(batch) >= 15:
                    process_batch(driver, batch, writer)
                    batch = []
                    driver.quit()  # Close the WebDriver
                    time.sleep(randint(420, 540))  # Random sleep between 7 and 9 minutes (420 and 540 seconds)
                    driver = webdriver.Chrome()  # Reopen the WebDriver

            # Process any remaining URLs
            if batch:
                process_batch(driver, batch, writer)

    # Close the WebDriver
    driver.quit()

try:
    # Process the CSV file and scrape text data
    process_csv('transcripts_list_data.csv', 'transcriptscraped_test_data.csv')

except WebDriverException as e:
    print("Blocked by website")
    print(e)
