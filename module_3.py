# module_3A (line 3 - 188) and module_3B (line 193 - 314)

# module_3A_MD&A_and_Q&A_extraction
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




# module_3B_individual_Qs_As
# Extracts the individual questions and answers and cleans text from 'transcripts_Qs_and_As.csv'

# import pandas as pd
# from bs4 import BeautifulSoup
# import re
#
# #Load the CSV files into DataFrames
# df = pd.read_csv('transcripts_Qs_and_As.csv')
# additional_data = pd.read_csv('transcripts_all_analysed_level1_grouped_modified_with_sector_updated.csv')
#
# # Combine text for each transcript ID
# combined_texts = df.groupby('ID')['transcript_text'].apply(lambda x: ' '.join(x)).reset_index()
#
# # Function to clean text
# def clean_text(text):
#
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
#     transcript_id = row['ID']
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
# merged_df.to_csv('Transcripts_Qs_and_As_Split.csv', index=False)



# Input to FinBERT here