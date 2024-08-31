# module 1.4 individual_Qs_As
# Extracts the individual questions and answers and cleans 'transcripts_Qs_and_As.csv'

import pandas as pd
from bs4 import BeautifulSoup
import re

#Load the CSV files into DataFrames
df = pd.read_csv('transcripts_Qs_and_As.csv')
additional_data = pd.read_csv('transcripts_all_analysed_level1_grouped_modified_with_sector_updated.csv')

# Combine text for each transcript ID
combined_texts = df.groupby('ID')['transcript_text'].apply(lambda x: ' '.join(x)).reset_index()

# Function to clean text
def clean_text(text):

    text = re.sub(r'(?i)good morning|good evening|good afternoon|good question|great question|'
                  r'Thanks for taking the question|Thanks for the question|Thank you|Thanks|Great', '', text)
    return text

# Function to extract and clean questions and answers
def extract_questions_answers(html_content):
    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Initialize variables to store questions and answers
    qa_list = []
    current_question = None
    current_answer = None

    # Iterate through paragraphs to find questions and answers
    for p in soup.find_all('p'):
        strong_tag = p.find('strong')
        if strong_tag:
            span_tag = strong_tag.find('span')
            if span_tag:
                span_class = span_tag.get('class')
                if span_class and 'question' in span_class[0]:
                    if current_question and current_answer:
                        qa_list.append(('Q', clean_text(current_question)))
                        qa_list.append(('A', clean_text(current_answer)))
                        current_answer = None
                    current_question = p.get_text(strip=True)
                elif span_class and 'answer' in span_class[0]:
                    current_answer = p.get_text(strip=True)
            else:
                continue
        else:
            if current_answer:
                current_answer += " " + p.get_text(strip=True)
            elif current_question:
                current_question += " " + p.get_text(strip=True)

    # Append the last question-answer pair if any
    if current_question and current_answer:
        qa_list.append(('Q', clean_text(current_question)))
        qa_list.append(('A', clean_text(current_answer)))

    return qa_list


# Initialize list to store the extracted data
extracted_data = []

# Process each combined text
for _, row in combined_texts.iterrows():
    transcript_id = row['ID']
    html_content = row['transcript_text']
    print(f"Processing ID: {transcript_id}")
#    print(f"HTML Content: {html_content[:500]}...")  # Print the first 500 characters of the HTML content for debugging

    qa_list = extract_questions_answers(html_content)
    if not qa_list:
        print(f"No Q&A pairs found for ID: {transcript_id}")

    for q_a, text in qa_list:
        # Filter out lines containing 'next question' and lines with fewer than ten words
        if 'next question' in text.lower() or len(text.split()) < 10:
            continue
        # print(f"{q_a}: {text}")  # Print the question/answer for debugging
        extracted_data.append({
            'id': transcript_id,
            'Q/A': q_a,
            'Q_A_text': text
        })

# Convert the extracted data to a DataFrame
extracted_df = pd.DataFrame(extracted_data)

# Print columns of additional_data to verify column names
# print("Columns in additional_data:", additional_data.columns)

# Rename 'ID' column in additional_data to 'id' for consistency
additional_data.rename(columns={'ID': 'id'}, inplace=True)

# Check for the existence of 'id' column
if 'id' not in additional_data.columns:
    raise KeyError("'id' column not found in additional_data")

# Define the columns to add
columns_to_add = ['Company_Name', 'Ticker', 'GICS Sector', 'Text', 'QUARTER', 'QTR', 'day_date_formatted']

# Check if all columns to add exist in additional_data
missing_columns = [col for col in columns_to_add if col not in additional_data.columns]
if missing_columns:
    raise KeyError(f"Columns {missing_columns} not found in additional_data")

# Aggregate additional_data to ensure one row per 'id'
aggregated_additional_data = additional_data.groupby('id')[columns_to_add].first().reset_index()

# Merge with the additional data based on 'id' column
merged_df = extracted_df.merge(aggregated_additional_data, on='id', how='left')

# Reorder columns to place the new columns after 'id'
columns_order = ['id'] + columns_to_add + ['Q/A', 'Q_A_text']
merged_df = merged_df[columns_order]

# Write the merged data to a new CSV file
merged_df.to_csv('Transcripts_Qs_and_As_Split.csv', index=False)



# Input to FinBERT here


def create_finbert_input_file():
    # Load the existing 'Transcripts_Qs_and_As_Split.csv' into a DataFrame
    df_split = pd.read_csv('Transcripts_Qs_and_As_Split.csv')

    # Select the relevant columns and rename them as per the requirement
    finbert_df = df_split[['id', 'Company_Name', 'Ticker', 'day_date_formatted', 'Text', 'Q/A', 'Q_A_text']].copy()
    finbert_df.rename(columns={
        'id': 'ID',
        'Company_Name': 'Company_AName',
        'day_date_formatted': 'Date',
        'Q/A': 'Call_Section',
        'Q_A_text': 'Transcript_Text'
    }, inplace=True)

    # Write the DataFrame to a new CSV file
    finbert_df.to_csv('ECC_FinBERT_Input.csv', index=False)
    print("ECC_FinBERT_Input.csv has been created successfully.")

# Call the function to create the FinBERT input file
create_finbert_input_file()
