
# module 1.3 MD&A_and_Q&A_extraction
# extracts the MD&A and Q&A sections in HTML format from the files 'transcriptscraped_test_data.csv'
# writes output to two files:
# (1) both MD&A_and_Q&A to 'transcripts.csv'
# (2) Q&A only to: 'transcripts_Qs_and_As.csv'


import pandas as pd
from bs4 import BeautifulSoup
import os


# Function to extract text between tags or provide notification if not found
def extract_text(data, start_tag, alt_start_tag, end_tag, alt_end_tag):
    start_index = data.find(start_tag)
    if start_index == -1:
        start_index = data.find(alt_start_tag)
        if start_index == -1:
            return "Tag not found"

    end_index = data.find(end_tag)
    if end_index == -1:
        end_index = data.find(alt_end_tag)
        if end_index == -1:
            return "Tag not found"

    text = data[start_index:end_index]
    soup = BeautifulSoup(text, 'html.parser')
    return soup.get_text(strip=True)


# Function to extract raw HTML between tags or provide notification if not found
def extract_html(data, start_tag, alt_start_tag, end_tag, alt_end_tag):
    start_index = data.find(start_tag)
    if start_index == -1:
        start_index = data.find(alt_start_tag)
        if start_index == -1:
            return "Tag not found"

    end_index = data.find(end_tag)
    if end_index == -1:
        end_index = data.find(alt_end_tag)
        if end_index == -1:
            return "Tag not found"

    return data[start_index:end_index + len(end_tag)]


# Define the chunk size
chunk_size = 8000


# Function to split text into chunks
def split_text_into_chunks(text):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

# Read CSV file
#Part1 below
input_csv = 'transcriptscraped_test_data.csv'

df = pd.read_csv(input_csv)

# Output file names
output_file = 'transcripts.csv'
output_qa_file = 'transcripts_Qs_and_As.csv'

# Remove output files if they exist (to avoid appending to old data during testing)
if os.path.exists(output_file):
    os.remove(output_file)
if os.path.exists(output_qa_file):
    os.remove(output_qa_file)

# Iterate over unique IDs
for id_val in df['id'].unique():
    # Filter data for the current ID
    df_id = df[df['id'] == id_val]

    # Get values
    company_name_val = df_id['company_name'].iloc[0]
    ticker_val = df_id['ticker'].iloc[0]
    date_val = df_id['date'].iloc[0]
    text_val = df_id['text'].iloc[0]
    transcript_text = df_id['transcript_text'].str.cat(
        sep=' ')  # Concatenate all transcript texts

    # Extract company statement text
    company_statement = extract_text(transcript_text,
                                     '<strong>Company Participants</strong>',
                                     '<strong>Corporate Participants</strong>',
                                     '<strong>Question-and-Answer Session</strong>',
                                     '<strong>Question-and-Answer Session</strong>')

    # Extract Q&A session text
    q_and_a = extract_text(transcript_text,
                           '<strong>Question-and-Answer Session</strong>',
                           '<strong>Question-and-Answer Session</strong>',
                           'twitContent',
                           'twitContent')

    # Split texts into chunks
    company_chunks = split_text_into_chunks(company_statement)
    qa_chunks = split_text_into_chunks(q_and_a)

    # Create DataFrame for company statement
    df_company = pd.DataFrame({'ID': id_val,
                               'Company Name': company_name_val,
                               'Ticker': ticker_val,
                               'Date': date_val,
                               'text': text_val,
                               'call_section': 'company_statement',
                               'transcript_text': company_chunks})

    # Create DataFrame for Q&A session
    df_qa = pd.DataFrame({'ID': id_val,
                          'Company Name': company_name_val,
                          'Ticker': ticker_val,
                          'Date': date_val,
                          'text': text_val,
                          'call_section': 'Q&A Session',
                          'transcript_text': qa_chunks})

    # Concatenate DataFrames
    df_concatenated = pd.concat([df_company, df_qa], ignore_index=True)

    # Write DataFrame to CSV with header
    if not os.path.exists(output_file):
        df_concatenated.to_csv(output_file, mode='w', index=False, header=True)
    else:
        df_concatenated.to_csv(output_file, mode='a', index=False,
                               header=False)


# New function to write Q&A data to a separate CSV file
def write_q_and_a_html_to_csv():
    # Read the same input CSV file again
    df = pd.read_csv(input_csv)

    all_q_and_a_html = []

    for id_val in df['id'].unique():
        # Filter data for the current ID
        df_id = df[df['id'] == id_val]

        # Get values
        company_name_val = df_id['company_name'].iloc[0]
        ticker_val = df_id['ticker'].iloc[0]
        date_val = df_id['date'].iloc[0]
        text_val = df_id['text'].iloc[0]
        transcript_text = df_id['transcript_text'].str.cat(
            sep=' ')  # Concatenate all transcript texts

        # Extract Q&A session HTML
        q_and_a_html = extract_html(transcript_text,
                                    '<strong>Question-and-Answer Session</strong>',
                                    '<strong>Question-and-Answer Session</strong>',
                                    'twitContent',
                                    'twitContent')

        # Split texts into chunks
        qa_chunks = split_text_into_chunks(q_and_a_html)

        # Create DataFrame for Q&A session HTML
        df_qa_html = pd.DataFrame({'ID': id_val,
                                   'Company Name': company_name_val,
                                   'Ticker': ticker_val,
                                   'Date': date_val,
                                   'text': text_val,
                                   'call_section': 'Q&A Session',
                                   'transcript_text': qa_chunks})

        # Collect all Q&A data
        all_q_and_a_html.append(df_qa_html)

    # Concatenate all Q&A data and write to a separate CSV with header
    if all_q_and_a_html:
        df_all_q_and_a_html = pd.concat(all_q_and_a_html, ignore_index=True)
        if not os.path.exists(output_qa_file):
            df_all_q_and_a_html.to_csv(output_qa_file, mode='w', index=False,
                                       header=True)
        else:
            df_all_q_and_a_html.to_csv(output_qa_file, mode='a', index=False,
                                       header=False)


# Call function to write Q&A data to the new CSV file
write_q_and_a_html_to_csv()




