
#STEP_1
# Webscraping lists of earnings call transcripts id data for later use
# Accesses SeekingAlpha API endpoint. Transcripts data presents as list of JSON objects.
# This is the one BH Sat 13 Jul
# from bs4 import BeautifulSoup
# import csv
# import time
# from selenium import webdriver
# import json
#
# from random import randint
#
# # Initialize Chrome WebDriver
# driver = webdriver.Chrome()
#
# # Loop through pages
# # Enter page range. Caution: Limit range to prevent blocking
# for page_number in range(300,301):
#
#     # SeekingAlpha API endpoint
#     # Construct URL
#     url = f"https://seekingalpha.com/api/v3/articles?filter[category]=earnings%3A%3Aearnings-call-transcripts&filter[since]=0&filter[until]=0&include=author%2CprimaryTickers%2CsecondaryTickers&isMounting=true&page[size]=50&page[number]={page_number}"
#
#     # Navigate to the URL
#     driver.get(url)
#     time.sleep(randint(4, 9))  # Adjust this delay as needed to ensure the page loads completely
#
#     # Extract page content - JSON list
#     page_content = driver.page_source
#     soup = BeautifulSoup(page_content, 'html.parser')
#     json_data = json.loads(soup.body.text)
#
#     # Extract data and append to CSV
#     with open('transcripts_list_data.csv', 'a', newline='') as csvfile:
#         fieldnames = ['id', 'company_name', 'ticker', 'text', 'date']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#         for item in json_data['data']:
#             id = item['id']
#             title = item['attributes']['title']
#             company_name, ticker, text = title.split('(')[0].strip(), \
#                                           title.split('(')[1].split(')')[0], title.split('(')[1].split(')')[
#                                               1].strip()
#             date = item['attributes']['publishOn']
#
#             writer.writerow(
#                 {'id': id, 'company_name': company_name, 'ticker': ticker,
#                  'text': text, 'date': date})
#
#     time.sleep(randint(4, 9))
#
# print("Data has been extracted and written to 'transcripts_list_data.csv'.")

#?????????????????????????????????????????
# This is the updated one Fri 19Jul 00.33 It works!
# from bs4 import BeautifulSoup
# import csv
# import time
# from selenium import webdriver
# import json
# from random import randint
#
# # Load S&P 500 companies
# sp500_companies = set()
# with open('S&P 500 Index Stocks List.csv', 'r') as spfile:
#     spreader = csv.DictReader(spfile)
#     for row in spreader:
#         sp500_companies.add(row['Symbol'])
#
# # Initialize Chrome WebDriver
# driver = webdriver.Chrome()
#
# # Open the output CSV file in write mode and write the headers
# with open('transcripts_list_data.csv', 'w', newline='') as csvfile:
#     fieldnames = ['id', 'company_name', 'ticker', 'text', 'date', 'S&P500_Company']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#
# # Loop through pages
# for page_number in range(300, 301):
#
#     # SeekingAlpha API endpoint
#     url = f"https://seekingalpha.com/api/v3/articles?filter[category]=earnings%3A%3Aearnings-call-transcripts&filter[since]=0&filter[until]=0&include=author%2CprimaryTickers%2CsecondaryTickers&isMounting=true&page[size]=50&page[number]={page_number}"
#
#     # Navigate to the URL
#     driver.get(url)
#     time.sleep(randint(4, 9))  # Adjust this delay as needed to ensure the page loads completely
#
#     # Extract page content - JSON list
#     page_content = driver.page_source
#     soup = BeautifulSoup(page_content, 'html.parser')
#     json_data = json.loads(soup.body.text)
#
#     # Extract data and append to CSV
#     with open('transcripts_list_data.csv', 'a', newline='') as csvfile:
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#         for item in json_data['data']:
#             id = item['id']
#             title = item['attributes']['title']
#             company_name = title.split('(')[0].strip()
#             ticker = title.split('(')[1].split(')')[0]
#             text = title.split('(')[1].split(')')[1].strip()
#             date = item['attributes']['publishOn']
#
#             sp500_company = 'Yes' if ticker in sp500_companies else 'No'
#
#             writer.writerow(
#                 {'id': id, 'company_name': company_name, 'ticker': ticker,
#                  'text': text, 'date': date, 'S&P500_Company': sp500_company})
#
#     time.sleep(randint(4, 9))
#
# print("Data has been extracted and written to 'transcripts_list_data.csv'.")
#
#
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#ChatGPT Up date S&P500 in ‘transcripts_list_data.csv’
# from bs4 import BeautifulSoup
# import csv
# import time
# from selenium import webdriver
# import json
# from random import randint
#
# # Load S&P 500 companies
# sp500_companies = set()
# with open('S&P 500 Index Stocks List.csv', 'r') as spfile:
#     spreader = csv.DictReader(spfile)
#     for row in spreader:
#         sp500_companies.add(row['Symbol'])
#
# # Initialize Chrome WebDriver
# driver = webdriver.Chrome()
#
# # Open the output CSV file in write mode and write the headers
# output_file = 'transcripts_list_data.csv'
# with open(output_file, 'w', newline='') as csvfile:
#     fieldnames = ['id', 'company_name', 'ticker', 'text', 'date', 'S&P500_Company']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#
# # Loop through pages
# for page_number in range(300, 301):
#
#     # SeekingAlpha API endpoint
#     url = f"https://seekingalpha.com/api/v3/articles?filter[category]=earnings%3A%3Aearnings-call-transcripts&filter[since]=0&filter[until]=0&include=author%2CprimaryTickers%2CsecondaryTickers&isMounting=true&page[size]=50&page[number]={page_number}"
#
#     # Navigate to the URL
#     driver.get(url)
#     time.sleep(randint(4, 9))  # Adjust this delay as needed to ensure the page loads completely
#
#     # Extract page content - JSON list
#     page_content = driver.page_source
#     soup = BeautifulSoup(page_content, 'html.parser')
#     json_data = json.loads(soup.body.text)
#
#     # Extract data and append to CSV
#     with open(output_file, 'a', newline='') as csvfile:
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#         for item in json_data['data']:
#             id = item['id']
#             title = item['attributes']['title']
#             company_name = title.split('(')[0].strip()
#             ticker = title.split('(')[1].split(')')[0]
#             text = title.split('(')[1].split(')')[1].strip()
#             date = item['attributes']['publishOn']
#
#             sp500_company = 'Yes' if ticker in sp500_companies else 'No'
#
#             writer.writerow(
#                 {'id': id, 'company_name': company_name, 'ticker': ticker,
#                  'text': text, 'date': date, 'S&P500_Company': sp500_company})
#
#     time.sleep(randint(4, 9))
#
# # Filter out rows where 'S&P500_Company' is 'No'
# with open(output_file, 'r') as csvfile:
#     reader = csv.DictReader(csvfile)
#     filtered_rows = [row for row in reader if row['S&P500_Company'] == 'Yes']
#
# # Write the filtered data back to the file
# with open(output_file, 'w', newline='') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(filtered_rows)
#
# print("Data has been extracted and written to 'transcripts_list_data.csv'.")






#?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
#Step 2
# Extracting the individual S&P500 transcripts
# Chat GPT Fri 26 Apr 16.25
# To achieve scraping in batches with reconnection between each batch,
# you can modify your code to close and reopen the Selenium WebDriver after each batch.
# Here's the modified version of your code:
# Back to line 1323 for the manual version.
#This is the one It works Sat 13Jul : Requires file 'transcript_data_test_urls_data.csv' (Maby 'transcripts_list_data.csv' will do (cut down in no of ids))
# import csv
# from selenium import webdriver
# from bs4 import BeautifulSoup
# import time
# from random import randint
# from selenium.common.exceptions import WebDriverException
#
#
# # Function to scrape text data from a single URL using BeautifulSoup
# def scrape_text(driver, url):
#     time.sleep(randint(4, 9))  # Random sleep between 4 and 9 seconds
#     driver.get(url)
#     try:
#         page_content = driver.page_source
#         soup = BeautifulSoup(page_content, 'html.parser')
#         text_element = soup.find('body')
#         if text_element:
#             transcript_text = text_element.get_text()
#         else:
#             transcript_text = None
#         return transcript_text
#     except Exception as e:
#         print(f"Error occurred while scraping text from URL: {url}")
#         print(e)
#         return None
#
#
# # Function to process a batch of URLs and scrape text data
# def process_batch(driver, batch, writer):
#     for row in batch:
#         id = row['id']
#         company_name = row['company_name']
#         ticker = row['ticker']
#         date = row['date']
#         text = row['text']
#
#         url = f"https://seekingalpha.com/api/v3/articles/{id}?include=author%2CprimaryTickers%2CsecondaryTickers%2CotherTags%2Cpresentations%2Cpresentations.slides%2Cauthor.authorResearch%2Cauthor.userBioTags%2Cco_authors%2CpromotedService%2Csentiments"
#         scraped_text = scrape_text(driver, url)
#
#         if scraped_text:
#             text_chunks = [scraped_text[i:i + 8000] for i in
#                            range(0, len(scraped_text), 8000)]
#             for chunk in text_chunks:
#                 writer.writerow(
#                     {'id': id, 'company_name': company_name, 'ticker': ticker,
#                      'date': date, 'text': text, 'transcript_text': chunk})
#         else:
#             writer.writerow(
#                 {'id': id, 'company_name': company_name, 'ticker': ticker,
#                  'date': date, 'text': text, 'transcript_text': ''})
#
#
# # Function to process the CSV file and scrape text data
# # input and output csv : See line 151 below
# def process_csv(input_csv, output_csv):
#     # Open the WebDriver
#     driver = webdriver.Chrome()
#
#     with open(input_csv, 'r', newline='', encoding='utf-8') as csvfile:
#         reader = csv.DictReader(csvfile)
#         with open(output_csv, 'a', newline='', encoding='utf-8') as outfile:
#             fieldnames = ['id', 'company_name', 'ticker', 'date', 'text',
#                           'transcript_text']
#             writer = csv.DictWriter(outfile, fieldnames=fieldnames)
#             writer.writeheader()
#
#             batch = []
#             for row in reader:
#                 batch.append(row)
#                 if len(batch) >= 15:
#                     process_batch(driver, batch, writer)
#                     batch = []
#                     driver.quit()  # Close the WebDriver
#                     time.sleep(randint(420,
#                                        540))  # Random sleep between 7 and 9 minutes (420 and 540 seconds)
#                     driver = webdriver.Chrome()  # Reopen the WebDriver
#
#             # Process any remaining URLs
#             if batch:
#                 process_batch(driver, batch, writer)
#
#     # Close the WebDriver
#     driver.quit()
#
#
# try:
#     # Process the CSV file and scrape text data
#     # process_csv('transcript_data_test_urls_data.csv',
#     #             'transcriptscraped_test_data.csv')
#     #BH 19JUl
#     process_csv('transcripts_list_data.csv',
#                 'transcriptscraped_test_data.csv')
#
# except WebDriverException as e:
#     print("Blocked by website")
#     print(e)










# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Step 3 : Requires file: 'transcriptscraped_test_data_testing.csv'
# Splitting out transcripts to Q&A and company_statement (also removes HTML tags)
#Line 1232 in EarningsCallTranscripts.py

# ChatGPT Tues 10Apr 2024 Re Iterating over all id’s in 'transcriptscraped_test_data_testing.
# This is the one that opens the webscraped raw transcripts files and extract them into MFD&A and Q&A in plain text(i Think) BH Sat 13 Jul
# import pandas as pd
# from bs4 import BeautifulSoup
# import csv
#
#
# # Function to extract text between tags or provide notification if not found
# def extract_text(data, start_tag, alt_start_tag, end_tag, alt_end_tag):
#     start_index = data.find(start_tag)
#     if start_index == -1:
#         start_index = data.find(alt_start_tag)
#         if start_index == -1:
#             return "Tag not found"
#
#     end_index = data.find(end_tag)
#     if end_index == -1:
#         end_index = data.find(alt_end_tag)
#         if end_index == -1:
#             return "Tag not found"
#
#     text = data[start_index:end_index]
#     soup = BeautifulSoup(text, 'html.parser')
#     return soup.get_text(strip=True)
#
#
# # Define the chunk size
# chunk_size = 8000
#
#
# # Function to split text into chunks
# def split_text_into_chunks(text):
#     return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
#
#
# # Read CSV file
# input_csv = 'transcriptscraped_test_data_testing.csv'
# df = pd.read_csv(input_csv)
#
# # Iterate over unique IDs
# for id_val in df['id'].unique():
#     # Filter data for the current ID
#     df_id = df[df['id'] == id_val]
#
#     # Get values
#     company_name_val = df_id['company_name'].iloc[0]
#     ticker_val = df_id['ticker'].iloc[0]
#     date_val = df_id['date'].iloc[0]
#     text_val = df_id['text'].iloc[0]
#     transcript_text = df_id['transcript_text'].str.cat(
#         sep=' ')  # Concatenate all transcript texts
#
#     # Extract company statement text
#     company_statement = extract_text(transcript_text,
#                                      '<strong>Company Participants</strong>',
#                                      '<strong>Corporate Participants</strong>',
#                                      '<strong>Question-and-Answer Session</strong>',
#                                      '<strong>Question-and-Answer Session</strong>')
#
#     # Extract Q&A session text
#     q_and_a = extract_text(transcript_text,
#                            '<strong>Question-and-Answer Session</strong>',
#                            '<strong>Question-and-Answer Session</strong>',
#                            'twitContent',
#                            'twitContent')
#
#     # Split texts into chunks
#     company_chunks = split_text_into_chunks(company_statement)
#     qa_chunks = split_text_into_chunks(q_and_a)
#
#     # Create DataFrame for company statement
#     df_company = pd.DataFrame({'ID': id_val,
#                                'Company Name': company_name_val,
#                                'Ticker': ticker_val,
#                                'Date': date_val,
#                                'text': text_val,
#                                'call_section': 'company_statement',
#                                'transcript_text': company_chunks})
#
#     # Create DataFrame for Q&A session
#     df_qa = pd.DataFrame({'ID': id_val,
#                           'Company Name': company_name_val,
#                           'Ticker': ticker_val,
#                           'Date': date_val,
#                           'text': text_val,
#                           'call_section': 'Q&A Session',
#                           'transcript_text': qa_chunks})
#
#     # Concatenate DataFrames
#     df_concatenated = pd.concat([df_company, df_qa], ignore_index=True)
#
#     # Write DataFrame to CSV
#     df_concatenated.to_csv('transcripts.csv', mode='a', index=False,
#                            header=False)
#












#  Questions and Answers all below
# sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss
# Questions and answers spearately
# Qs and As STEP 1
# Extracting Questions and Answers Separetly - Part 1 (Line 2479 in EarningsCallTranscripts(V1).py)
# This is the one BH Sat 13 Jul. Requires file: 'transcriptscraped_test_data_testing.csv'
#ChatGPT  Q and A extraction problem Sun 08 Jul  09.36  Use this one. Note:This is the original code with an additional new function at the end
#Third version with headings added This works (the earlier two versions worked also but
# No1 wrote the output to the new file in plain text and no headings on either output file
# No2 wrote the output correctly in HTML format to the new file, but no headings on either output file
# See the ChatGPT word document!
# back to line 2140 (this code goes to 2669)
#This version below has headers added and works good
# This code extracts the individual questions and answers from the files 'transcriptscraped_test_data_master_Part1_12Apr.csv' etc

# import pandas as pd
# from bs4 import BeautifulSoup
# import os
#
#
# # Function to extract text between tags or provide notification if not found
# def extract_text(data, start_tag, alt_start_tag, end_tag, alt_end_tag):
#     start_index = data.find(start_tag)
#     if start_index == -1:
#         start_index = data.find(alt_start_tag)
#         if start_index == -1:
#             return "Tag not found"
#
#     end_index = data.find(end_tag)
#     if end_index == -1:
#         end_index = data.find(alt_end_tag)
#         if end_index == -1:
#             return "Tag not found"
#
#     text = data[start_index:end_index]
#     soup = BeautifulSoup(text, 'html.parser')
#     return soup.get_text(strip=True)
#
#
# # Function to extract raw HTML between tags or provide notification if not found
# def extract_html(data, start_tag, alt_start_tag, end_tag, alt_end_tag):
#     start_index = data.find(start_tag)
#     if start_index == -1:
#         start_index = data.find(alt_start_tag)
#         if start_index == -1:
#             return "Tag not found"
#
#     end_index = data.find(end_tag)
#     if end_index == -1:
#         end_index = data.find(alt_end_tag)
#         if end_index == -1:
#             return "Tag not found"
#
#     return data[start_index:end_index + len(end_tag)]
#
#
# # Define the chunk size
# chunk_size = 8000
#
#
# # Function to split text into chunks
# def split_text_into_chunks(text):
#     return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
#
# # Read CSV file
# # input_csv = 'transcriptscraped_test_data_testing.csv'
# #BH Sun 07JUl
# #Part1 below
# # input_csv = 'transcriptscraped_test_data_master_Part1_12Apr.csv'
# # input_csv = 'transcriptscraped_test_data_Sat03May_1930 to 2230_Part6_B.csv'
# #input_csv = 'transcriptscraped_test_data_master_Part1_12Apr.csv'
# input_csv = 'transcriptscraped_test_data.csv'
#
# df = pd.read_csv(input_csv)
#
# # Output file names
# output_file = 'transcripts.csv'
# output_qa_file = 'transcripts_Qs_and_As.csv'
#
# # Remove output files if they exist (to avoid appending to old data during testing)
# if os.path.exists(output_file):
#     os.remove(output_file)
# if os.path.exists(output_qa_file):
#     os.remove(output_qa_file)
#
# # Iterate over unique IDs
# for id_val in df['id'].unique():
#     # Filter data for the current ID
#     df_id = df[df['id'] == id_val]
#
#     # Get values
#     company_name_val = df_id['company_name'].iloc[0]
#     ticker_val = df_id['ticker'].iloc[0]
#     date_val = df_id['date'].iloc[0]
#     text_val = df_id['text'].iloc[0]
#     transcript_text = df_id['transcript_text'].str.cat(
#         sep=' ')  # Concatenate all transcript texts
#
#     # Extract company statement text
#     company_statement = extract_text(transcript_text,
#                                      '<strong>Company Participants</strong>',
#                                      '<strong>Corporate Participants</strong>',
#                                      '<strong>Question-and-Answer Session</strong>',
#                                      '<strong>Question-and-Answer Session</strong>')
#
#     # Extract Q&A session text
#     q_and_a = extract_text(transcript_text,
#                            '<strong>Question-and-Answer Session</strong>',
#                            '<strong>Question-and-Answer Session</strong>',
#                            'twitContent',
#                            'twitContent')
#
#     # Split texts into chunks
#     company_chunks = split_text_into_chunks(company_statement)
#     qa_chunks = split_text_into_chunks(q_and_a)
#
#     # Create DataFrame for company statement
#     df_company = pd.DataFrame({'ID': id_val,
#                                'Company Name': company_name_val,
#                                'Ticker': ticker_val,
#                                'Date': date_val,
#                                'text': text_val,
#                                'call_section': 'company_statement',
#                                'transcript_text': company_chunks})
#
#     # Create DataFrame for Q&A session
#     df_qa = pd.DataFrame({'ID': id_val,
#                           'Company Name': company_name_val,
#                           'Ticker': ticker_val,
#                           'Date': date_val,
#                           'text': text_val,
#                           'call_section': 'Q&A Session',
#                           'transcript_text': qa_chunks})
#
#     # Concatenate DataFrames
#     df_concatenated = pd.concat([df_company, df_qa], ignore_index=True)
#
#     # Write DataFrame to CSV with header
#     if not os.path.exists(output_file):
#         df_concatenated.to_csv(output_file, mode='w', index=False, header=True)
#     else:
#         df_concatenated.to_csv(output_file, mode='a', index=False,
#                                header=False)
#
#
# # New function to write Q&A data to a separate CSV file
# def write_q_and_a_html_to_csv():
#     # Read the same input CSV file again
#     df = pd.read_csv(input_csv)
#
#     all_q_and_a_html = []
#
#     for id_val in df['id'].unique():
#         # Filter data for the current ID
#         df_id = df[df['id'] == id_val]
#
#         # Get values
#         company_name_val = df_id['company_name'].iloc[0]
#         ticker_val = df_id['ticker'].iloc[0]
#         date_val = df_id['date'].iloc[0]
#         text_val = df_id['text'].iloc[0]
#         transcript_text = df_id['transcript_text'].str.cat(
#             sep=' ')  # Concatenate all transcript texts
#
#         # Extract Q&A session HTML
#         q_and_a_html = extract_html(transcript_text,
#                                     '<strong>Question-and-Answer Session</strong>',
#                                     '<strong>Question-and-Answer Session</strong>',
#                                     'twitContent',
#                                     'twitContent')
#
#         # Split texts into chunks
#         qa_chunks = split_text_into_chunks(q_and_a_html)
#
#         # Create DataFrame for Q&A session HTML
#         df_qa_html = pd.DataFrame({'ID': id_val,
#                                    'Company Name': company_name_val,
#                                    'Ticker': ticker_val,
#                                    'Date': date_val,
#                                    'text': text_val,
#                                    'call_section': 'Q&A Session',
#                                    'transcript_text': qa_chunks})
#
#         # Collect all Q&A data
#         all_q_and_a_html.append(df_qa_html)
#
#     # Concatenate all Q&A data and write to a separate CSV with header
#     if all_q_and_a_html:
#         df_all_q_and_a_html = pd.concat(all_q_and_a_html, ignore_index=True)
#         if not os.path.exists(output_qa_file):
#             df_all_q_and_a_html.to_csv(output_qa_file, mode='w', index=False,
#                                        header=True)
#         else:
#             df_all_q_and_a_html.to_csv(output_qa_file, mode='a', index=False,
#                                        header=False)
#
#
# # Call the new function to write Q&A data to the new CSV file
# write_q_and_a_html_to_csv()











# ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss
# Qs and As:  STEP 2 remove specific text and lines from Q-A file
# This is the one BH Sat 13 Jul
# Extracting Questions and Answers Seperatly - Part 2

# ChatGPT remove specific text and lines from Q-A file Fri 05Jul 23.45 (line 2269 in EarningsCallTranscripts(V1).py)
# go to line 2479 (this code goes to 2263)
# import pandas as pd
# from bs4 import BeautifulSoup
# import re
#
# #Load the CSV files into DataFrames
# # df = pd.read_csv('transcriptscraped_test_data_testing.csv')
# # df = pd.read_csv('C:/Users/mbjhi/PycharmProjects/Wk1Assign/Transcripts_Q_A/Part1/transcriptscraped_test_data_master_Part1_12Apr.csv')
# # df = pd.read_csv('C:/Users/mbjhi/PycharmProjects/Wk1Assign/Transcripts_Q_A/Part1/transcriptscraped_test_data_testing.csv')
# df = pd.read_csv('transcripts_Qs_and_As.csv')  # NOTE: BH 19 Jul Changed ID in input file to lower case id
# additional_data = pd.read_csv('transcripts_all_analysed_level1_grouped_modified_with_sector_updated.csv')
#
# # Combine text for each transcript ID
# combined_texts = df.groupby('id')['transcript_text'].apply(lambda x: ' '.join(x)).reset_index()
#
# # Function to clean text  (BH This is the original that works just not perfectly!)
# def clean_text(text):
#     # Remove 'good morning' or 'good evening' regardless of case
#     #text = re.sub(r'(?i)good morning|good evening', '', text)
#     # BH
#     #text = re.sub(r'(?i)good morning|good evening|good afternoon|good question|great question|Thanks for taking the question|Thanks for the question|Thank you|Thanks|Great', '', text)
#     text = re.sub(r'(?i)good morning|good evening|good afternoon|good question|great question|'
#                   r'Thanks for taking the question|Thanks for the question|Thank you|Thanks|Great', '', text)
#     return text
#
# # Function to extract and clean questions and answers
# def extract_questions_answers(html_content):
#     # Parse the HTML content
#     soup = BeautifulSoup(html_content, 'html.parser')
#
#     # Initialize variables to store questions and answers
#     qa_list = []
#     current_question = None
#     current_answer = None
#
#     # Iterate through paragraphs to find questions and answers
#     for p in soup.find_all('p'):
#         strong_tag = p.find('strong')
#         if strong_tag:
#             span_tag = strong_tag.find('span')
#             if span_tag:
#                 span_class = span_tag.get('class')
#                 if span_class and 'question' in span_class[0]:
#                     if current_question and current_answer:
#                         qa_list.append(('Q', clean_text(current_question)))
#                         qa_list.append(('A', clean_text(current_answer)))
#                         current_answer = None
#                     current_question = p.get_text(strip=True)
#                 elif span_class and 'answer' in span_class[0]:
#                     current_answer = p.get_text(strip=True)
#             else:
#                 continue
#         else:
#             if current_answer:
#                 current_answer += " " + p.get_text(strip=True)
#             elif current_question:
#                 current_question += " " + p.get_text(strip=True)
#
#     # Append the last question-answer pair if any
#     if current_question and current_answer:
#         qa_list.append(('Q', clean_text(current_question)))
#         qa_list.append(('A', clean_text(current_answer)))
#
#     return qa_list
#
#
# # Initialize list to store the extracted data
# extracted_data = []
#
# # Process each combined text
# for _, row in combined_texts.iterrows():
#     transcript_id = row['id']
#     html_content = row['transcript_text']
#     print(f"Processing ID: {transcript_id}")
#     print(f"HTML Content: {html_content[:500]}...")  # Print the first 500 characters of the HTML content for debugging
#
#     qa_list = extract_questions_answers(html_content)
#     if not qa_list:
#         print(f"No Q&A pairs found for ID: {transcript_id}")
#
#     for q_a, text in qa_list:
#         # Filter out lines containing 'next question' and lines with fewer than ten words
#         if 'next question' in text.lower() or len(text.split()) < 10:
#             continue
#         print(f"{q_a}: {text}")  # Print the question/answer for debugging
#         extracted_data.append({
#             'id': transcript_id,
#             'Q/A': q_a,
#             'Q_A_text': text
#         })
#
# # Convert the extracted data to a DataFrame
# extracted_df = pd.DataFrame(extracted_data)
#
# # Print columns of additional_data to verify column names
# print("Columns in additional_data:", additional_data.columns)
#
# # Rename 'ID' column in additional_data to 'id' for consistency
# additional_data.rename(columns={'ID': 'id'}, inplace=True)
#
# # Check for the existence of 'id' column
# if 'id' not in additional_data.columns:
#     raise KeyError("'id' column not found in additional_data")
#
# # Define the columns to add
# columns_to_add = ['Company_Name', 'Ticker', 'GICS Sector', 'Text', 'QUARTER', 'QTR', 'day_date_formatted']
#
# # Check if all columns to add exist in additional_data
# missing_columns = [col for col in columns_to_add if col not in additional_data.columns]
# if missing_columns:
#     raise KeyError(f"Columns {missing_columns} not found in additional_data")
#
# # Aggregate additional_data to ensure one row per 'id'
# aggregated_additional_data = additional_data.groupby('id')[columns_to_add].first().reset_index()
#
# # Merge with the additional data based on 'id' column
# merged_df = extracted_df.merge(aggregated_additional_data, on='id', how='left')
#
# # Reorder columns to place the new columns after 'id'
# columns_order = ['id'] + columns_to_add + ['Q/A', 'Q_A_text']
# merged_df = merged_df[columns_order]
#
# # Write the merged data to a new CSV file
# merged_df.to_csv('Transcripts_Qs_and_As_part1.csv', index=False)



# FinBERT goes in here



# UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU

# ChatGPT Transcripts Qs and As combine and group individual files Fri 12Jul 0659
#
# Mon 15Jul
# Update to place output in same folder as py.charm and change name of fields
# Pg8
# import pandas as pd
# import os
#
# # Define the directory containing the CSV files (in the same location as the script)
# directory = 'FinBERT output files combined'
#
# # Define the fields to group by
# group_fields = ['ID', 'Call_Section']
#
# # Define the fields to sum
# sum_fields = ['count of +ve', 'count of -ve', 'count of neutral']
#
# # Define the fields to keep
# keep_fields = ['Company_AName', 'Ticker', 'Text']
#
# # Initialize an empty list to store the grouped DataFrames
# grouped_dataframes = []
#
# # Iterate over each file in the directory
# for filename in os.listdir(directory):
#     if filename.endswith('.csv'):
#         # Construct the full file path
#         file_path = os.path.join(directory, filename)
#
#         # Read the CSV file into a DataFrame
#         df = pd.read_csv(file_path)
#
#         # Ensure the sum fields are numeric
#         for field in sum_fields:
#             df[field] = pd.to_numeric(df[field], errors='coerce')
#
#         # Select the necessary fields
#         df = df[group_fields + sum_fields + keep_fields]
#
#         # Group the DataFrame by the specified fields and sum the required fields
#         grouped_df = df.groupby(group_fields + keep_fields)[sum_fields].sum().reset_index()
#
#         # Append the grouped DataFrame to the list
#         grouped_dataframes.append(grouped_df)
#
# # Concatenate all the grouped DataFrames
# combined_df = pd.concat(grouped_dataframes)
#
# # Group the combined DataFrame again to ensure proper aggregation
# combined_df = combined_df.groupby(group_fields + keep_fields)[sum_fields].sum().reset_index()
#
# # Rename the columns as required
# combined_df = combined_df.rename(columns={
#     'count of +ve': 'sum of +ve',
#     'count of -ve': 'sum of -ve',
#     'count of neutral': 'sum of neutral'
# })
#
# # Define the output file path
# # output_file_path = 'Qs_and_As_grouped.csv'
# #Bh change below 19 Jul 0912
# output_file_path = 'combined_file.csv'
#
# # Save the combined DataFrame to a new CSV file in the current working directory
# combined_df.to_csv(output_file_path, index=False)
#
# print(f"Grouping and combination of CSV files is complete. Output saved to '{output_file_path}'.")
#
# # Above works BH 19 Jul 0928




#ChatGPT new columns and update ‘GCIS_Sector’ ‘QTR’  and ‘day_date’ in file ‘combined.csv’ Fri 12 Jul

# import pandas as pd
#
# # Read the CSV file
# file_path = 'combined_file.csv'
# df = pd.read_csv(file_path)
#
# # Define the new columns with default values or empty strings
# df['GICS Sector'] = ''  # You can replace '' with default values if needed
# df['QTR'] = ''          # You can replace '' with default values if needed
# df['day_date'] = ''     # You can replace '' with default values if needed
# #BH added tone,price_chng_5day,price_chng_2day,price_chng_1day Fri 12 Jul
# df['tone'] = ''     # You can replace '' with default values if needed
# df['price_chng_5day'] = ''     # You can replace '' with default values if needed
# df['price_chng_2day'] = ''     # You can replace '' with default values if needed
# df['price_chng_1day'] = ''     # You can replace '' with default values if needed
#
#
# # Reorder columns to place the new columns between 'Call_Section' and 'Company_Aname'
# # columns = ['ID', 'Call_Section', 'GICS Sector', 'QTR', 'day_date', 'Company_AName', 'Ticker', 'Text', 'count of +ve', 'count of -ve', 'count of neutral', 'tone', 'price_chng_5day','price_chng_2day', 'price_chng_1day' ]
# # BH 19 JUl 0923
# columns = ['ID', 'Call_Section', 'GICS Sector', 'QTR', 'day_date', 'Company_AName', 'Ticker', 'Text', 'sum of +ve', 'sum of -ve', 'sum of neutral', 'tone', 'price_chng_5day','price_chng_2day', 'price_chng_1day' ]
#
# df = df[columns]
#
# # Save the modified DataFrame to a new CSV file
# output_file_path = 'updated_combined_file.csv'
# df.to_csv(output_file_path, index=False)
#
# print(f"Updated file saved as {output_file_path}")
#
# # All works to here (above) BH 19 Jul 09.36



#ChatGPT Update new columns GICS Sector, Day_Date, QTR in file combined 12Jul20.28

# import pandas as pd
#
# # Load the CSV files into DataFrames
# # df_combined = pd.read_csv('updated_combined_file.csv')
# # df_combined = pd.read_csv('updated_Qs_and_As_grouped.csv')
# df_combined = pd.read_csv('updated_combined_file.csv')
#
# df_transcripts = pd.read_csv('transcripts_all_analysed_level1_grouped_modified_with_sector_updated.csv')
#
# # Convert the 'ID' columns to strings to ensure they match in type
# df_combined['ID'] = df_combined['ID'].astype(str)
# df_transcripts['ID'] = df_transcripts['ID'].astype(str)
#
# # Group the transcripts DataFrame by 'ID'
# grouped_transcripts = df_transcripts.groupby('ID')
#
# # Function to update row with new data if available
# def update_row(row):
#     if row['ID'] in grouped_transcripts.groups:
#         # Get the group for this ID
#         group = grouped_transcripts.get_group(row['ID'])
#         # Use the first occurrence of each value for simplicity
#         row['GICS Sector'] = group['GICS Sector'].values[0]
#         row['day_date'] = group['day_date_formatted'].values[0]
#         row['QTR'] = group['QTR'].values[0]
#     return row
#
# # Apply the update_row function to each row in the combined DataFrame
# df_combined = df_combined.apply(update_row, axis=1)
#
# # Save the updated DataFrame to a new CSV file
# df_combined.to_csv('updated_Qs_and_As_grouped_updated.csv', index=False)

# #All works to here (above). BH 19 Jul 09.38


# ChatGPT Date fields check and ensure compatibility 13Jul    goes to line 1035

# import pandas as pd
# import os
#
#
# # Function to ensure date parsing and column creation
# def ensure_date_compatible(df, date_column, new_column_name='date_compatible'):
#     try:
#         df[new_column_name] = pd.to_datetime(df[date_column])
#         print(
#             f"'{date_column}' column successfully parsed and '{new_column_name}' field created.")
#     except Exception as e:
#         print(f"Error parsing '{date_column}' column: {e}")
#     return df
#
#
# # Load the combined file
# # combined_file_path = 'updated_combined_file_updated.csv'
# #BH 17 Jul 20.05
# combined_file_path = 'updated_Qs_and_As_grouped_updated.csv'
# combined_file = pd.read_csv(combined_file_path)
#
# # Parse the day_date column and create date_compatible field in combined file
# combined_file = ensure_date_compatible(combined_file, 'day_date')
#
# # Verify if date_compatible is in datetime format
# if pd.api.types.is_datetime64_any_dtype(combined_file['date_compatible']):
#     print("'date_compatible' field in combined file is in datetime format.")
# else:
#     print(
#         "'date_compatible' field in combined file is NOT in datetime format.")
#
# # Save the modified combined file
# combined_file.to_csv('updated_combined_file_with_compatible_date.csv',
#                      index=False)
#
# # Folder containing stock data files
# stock_data_folder = 'Stock_Data_Files'
#
# # Get a list of all stock data files
# stock_files = [f for f in os.listdir(stock_data_folder) if f.endswith('.csv')]
#
# # Iterate through each stock data file and create date_compatible field
# for stock_file in stock_files:
#     file_path = os.path.join(stock_data_folder, stock_file)
#     stock_df = pd.read_csv(file_path)
#
#     # Parse the Date column and create date_compatible field
#     stock_df = ensure_date_compatible(stock_df, 'Date')
#
#     # Verify if date_compatible is in datetime format
#     if pd.api.types.is_datetime64_any_dtype(stock_df['date_compatible']):
#         print(
#             f"'date_compatible' field in {stock_file} is in datetime format.")
#     else:
#         print(
#             f"'date_compatible' field in {stock_file} is NOT in datetime format.")
#
#     # Save the modified stock file
#     stock_df.to_csv(file_path, index=False)
#
# print(
#     "All files have been updated with 'date_compatible' fields and verified for datetime format.")


# All works to here. BH 19 Jul 09.41


# ChatGPT update price change columns in updated_combined_file_with_compatible_date.csv’ 14Jul 20.05

# import pandas as pd
# import os
#
# # Load the combined file
# combined_file_path = 'updated_combined_file_with_compatible_date.csv'
# combined_df = pd.read_csv(combined_file_path)
#
# # Define the folder containing stock data files
# stock_data_folder = 'Stock_Data_Files'
#
#
# # Function to calculate the fractional difference
# def calculate_fractional_difference(stock_df, ec_date):
#     try:
#         # Convert date columns to datetime
#         stock_df['date_compatible'] = pd.to_datetime(
#             stock_df['date_compatible'])
#         ec_date = pd.to_datetime(ec_date)
#
#         # Check if the earnings call date is in the stock data
#         if ec_date not in stock_df['date_compatible'].values:
#             return 'date_not_found'
#
#         # Get the index of the earnings call date
#         ec_index = stock_df[stock_df['date_compatible'] == ec_date].index[0]
#
#         # Get the close prices for the 5 days before and 5 days after
#         before_df = stock_df.iloc[ec_index - 5:ec_index]
#         after_df = stock_df.iloc[ec_index + 1:ec_index + 6]
#
#         # Check if there are enough days before and after the EC date
#         if len(before_df) < 5 or len(after_df) < 5:
#             return 'date_not_found'
#
#         # Calculate the average close prices
#         avg_before = before_df['Close'].mean()
#         avg_after = after_df['Close'].mean()
#
#         # Calculate the fractional difference
#         fractional_diff = (avg_after - avg_before) / avg_before
#         return round(fractional_diff, 3)
#     except Exception as e:
#         return 'date_not_found'
#
#
# # Iterate over each row in the combined file
# for idx, row in combined_df.iterrows():
#     ticker = row['Ticker']
#     ec_date = row['date_compatible']
#
#     # Construct the file path for the stock data file
#     stock_file_path = os.path.join(stock_data_folder, f'{ticker}.csv')
#
#     # Check if the stock data file exists
#     if not os.path.exists(stock_file_path):
#         combined_df.at[idx, 'price_chng_5day'] = 'date_not_found'
#         continue
#
#     # Load the stock data file
#     stock_df = pd.read_csv(stock_file_path)
#
#     # Calculate the fractional difference and update the combined file
#     fractional_diff = calculate_fractional_difference(stock_df, ec_date)
#     combined_df.at[idx, 'price_chng_5day'] = fractional_diff
#
# # Save the updated combined file
# combined_df.to_csv(combined_file_path, index=False)

# All works to here BH 19 JUl 09.44






# # ChatGPT Update tone in updated_combined_file_with_compatible_date.csv 14Jul21.25
import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('updated_combined_file_with_compatible_date.csv')

# Calculate the new 'tone' values
# df['tone'] = (df['count of +ve'] - df['count of -ve']) / (df['count of +ve'] + df['count of -ve'])
# BH 17Jul 20.16
df['tone'] = (df['sum of +ve'] - df['sum of -ve']) / (df['sum of +ve'] + df['sum of -ve'])

# Save the updated DataFrame back to a CSV file
df.to_csv('updated_combined_file_with_compatible_date.csv', index=False)

#All works to here BH 19 Jul 09.45