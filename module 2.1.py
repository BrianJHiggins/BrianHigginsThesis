"""
Implementation of FinBERT
Description
This module is run on Kaggle making use of the GPU P100 accelerator
Input 'Transcripts_Questions_Answers_Test_cleaned_7.csv'
the file contains the plain text questions and answers extracted
from Earnings Conference Call transcripts.
output file: 'earnings_calls_Kaggle_Test_q_a.csv'  The output consists of the input returned with
each question and answer (row) given sentiment classification scores.
Each Q and A can be inspected
Processor: (Kaggle) GPU P100 accelerator.
Total processing time for entire input is approx 11 hours

"""

from transformers import BertForSequenceClassification, BertTokenizer
import torch
import pandas as pd
import csv

classes = {0:'positive', 1:'negative', 2:'neutral'}

tokenizer = BertTokenizer.from_pretrained('ProsusAI/finbert')

model = BertForSequenceClassification.from_pretrained('ProsusAI/finbert')


def text_processing(text):
    txt = text
    tokens = tokenizer.encode_plus(txt, add_special_tokens=False)
    input_ids, token_type_ids, attention_mask = tokens['input_ids'], tokens['token_type_ids'], tokens['attention_mask']
    total_len = len(tokens['input_ids'])
    return input_ids, attention_mask, total_len
    tokens.keys()
# tokens.keys()

def chunk_text_to_window_size_and_predict_proba(input_ids, attention_mask,
                                                total_len):
    """
    This function splits the given input text into chunks of a specified window length,
    applies transformer model to each chunk and computes probabilities of each class for each chunk.
    The computed probabilities are then appended to a list.

    Args:
        input_ids (List[int]): List of token ids representing the input text.
        attention_mask (List[int]): List of attention masks corresponding to input_ids.
        total_len (int): Total length of the input_ids.

    Returns:
        proba_list (List[torch.Tensor]): List of probability tensors for each chunk.
    """
    proba_list = []

    start = 0
    window_length = 510

    loop = True
    while loop:
        end = start + window_length
        # If the end index exceeds total length, set the flag to False and adjust the end index
        if end >= total_len:
            loop = False
            end = total_len

        # 1 => Define the text chunk
        input_ids_chunk = input_ids[start: end]
        attention_mask_chunk = attention_mask[start: end]

        # 2 => Append [CLS] and [SEP]
        input_ids_chunk = [101] + input_ids_chunk + [102]
        attention_mask_chunk = [1] + attention_mask_chunk + [1]

        # 3 Convert regular python list to Pytorch Tensor
        input_dict = {
            'input_ids': torch.Tensor([input_ids_chunk]).long(),
            'attention_mask': torch.Tensor([attention_mask_chunk]).int()
        }

        outputs = model(**input_dict)
        probabilities = torch.nn.functional.softmax(outputs[0], dim=-1)
        proba_list.append(probabilities)
        start = end

    return proba_list

    # proba_list = chunk_text_to_window_size_and_predict_proba(input_ids, attention_mask, total_len)
    # print("This is the 'proba' list:", proba_list)


def get_mean_from_proba(proba_list):
    """
    This function computes the mean probabilities of class predictions over all the chunks.

    Args:
        proba_list (List[torch.Tensor]): List of probability tensors for each chunk.

    Returns:
        mean (torch.Tensor): Mean of the probabilities across all chunks.
    """

    # Ensures that gradients are not computed, saving memory
    with torch.no_grad():
        # Stack the list of tensors into a single tensor
        stacks = torch.stack(proba_list)

        # Resize the tensor to match the dimensions needed for mean computation
        stacks = stacks.resize(stacks.shape[0], stacks.shape[2])
        # print("This is 'stacks':", stacks) #BH Tue 16Apr 00.27

        # Compute the mean along the zeroth dimension (i.e., the chunk dimension)
        mean = stacks.mean(dim=0)

    return mean

# mean = get_mean_from_proba(proba_list)
# tensor([0.0767, 0.1188, 0.8045])

# torch.argmax(mean).item()
# mean


output_filename = './earnings_calls_Kaggle_Test_q_a.csv'

df = pd.read_csv(
    '/kaggle/input/transcripts-questions-answers-test-cleaned-7-csv/Transcripts_Questions_Answers_Test_cleaned_7.csv',
    encoding='utf-8')
with open(output_filename, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)

    csv_writer.writerow(
        ['ID', 'Company_AName', 'Ticker', 'Text', 'Call_Section',
         'Transcript_Text', 'sentiment', 'count of +ve', 'count of -ve',
         'count of neutral'])

    # Iterate over each row in the DataFrame
    for i, row in df.iterrows():
        # Extract relevant information from the current row
        ID = row['ID']
        Company_AName = row['Company_AName']
        Ticker = row['Ticker']
        Text = row['Text']
        Call_Section = row['Call_Section']
        Transcript_Text = row['Transcript_Text']
        # sentiment = row['sentiment']

        # Perform sentiment analysis on the text to get FinBERT sentiment
        # input_ids, attention_mask, total_len = text_processing(text)

        input_ids, attention_mask, total_len = text_processing(Transcript_Text)

        proba_list = chunk_text_to_window_size_and_predict_proba(input_ids,
                                                                 attention_mask,
                                                                 total_len)
        mean = get_mean_from_proba(proba_list)
        result_class = classes[torch.argmax(mean).item()]
        # print("This is the 'proba_list':",proba_list) # BH Tue 16Apr 20.08
        # Count of probability classes per line.

        # Initialize counters
        count_positive = 0
        count_negative = 0
        count_neutral = 0

        # Count the occurrences of each class
        for prob in proba_list:
            pred_class = torch.argmax(prob).item()
            if pred_class == 0:
                count_positive += 1
            elif pred_class == 1:
                count_negative += 1
            elif pred_class == 2:
                count_neutral += 1

        # Write the processed row to the output CSV file
        csv_writer.writerow(
            [ID, Company_AName, Ticker, Text, Call_Section, Transcript_Text,
             result_class, count_positive, count_negative, count_neutral])

        # Write the processed row to the output CSV file
        # csv_writer.writerow([phrase_id, sentiment, text, result_class])

        # Write the processed row to the output CSV file
        # csv_writer.writerow([ID, Company_AName, Ticker, Text, Call_Section, Transcript_Text, result_class])


