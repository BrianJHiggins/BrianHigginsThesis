
# module 3.2 update tone and stock price changes (5 parts below )

# PART 1 of 5
#new columns and update ‘GCIS_Sector’ ‘QTR’  and ‘day_date’ in file ‘combined.csv’ Fri 12 Jul
# update price change data and tone

import pandas as pd
import os

# Read the CSV file
file_path = 'combined_file.csv'
df = pd.read_csv(file_path)

# Define the new columns with default values or empty strings
df['GICS Sector'] = ''
df['QTR'] = ''
df['day_date'] = ''
df['tone'] = ''
df['price_chng_5day'] = ''
df['price_chng_2day'] = ''
df['price_chng_1day'] = ''


# Reorder columns to place the new columns between 'Call_Section' and 'Company_Aname'
# columns = ['ID', 'Call_Section', 'GICS Sector', 'QTR', 'day_date', 'Company_AName', 'Ticker', 'Text', 'count of +ve', 'count of -ve', 'count of neutral', 'tone', 'price_chng_5day','price_chng_2day', 'price_chng_1day' ]
columns = ['ID', 'Call_Section', 'GICS Sector', 'QTR', 'day_date', 'Company_AName', 'Ticker', 'Text', 'sum of +ve', 'sum of -ve', 'sum of neutral', 'tone', 'price_chng_5day','price_chng_2day', 'price_chng_1day' ]

df = df[columns]

# Save the modified DataFrame to a new CSV file
output_file_path = 'updated_combined_file.csv'
df.to_csv(output_file_path, index=False)

print(f"Updated file saved as {output_file_path}")

# PART 2
# Update new columns GICS Sector, Day_Date, QTR in file combined

# Load the CSV files into DataFrames
# df_combined = pd.read_csv('updated_combined_file.csv')
# df_combined = pd.read_csv('updated_Qs_and_As_grouped.csv')
df_combined = pd.read_csv('updated_combined_file.csv')

df_transcripts = pd.read_csv('transcripts_all_analysed_level1_grouped_modified_with_sector_updated.csv')

# Convert the 'ID' columns to strings to ensure they match in type
df_combined['ID'] = df_combined['ID'].astype(str)
df_transcripts['ID'] = df_transcripts['ID'].astype(str)

# Group the transcripts DataFrame by 'ID'
grouped_transcripts = df_transcripts.groupby('ID')

# Function to update row with new data if available
def update_row(row):
    if row['ID'] in grouped_transcripts.groups:
        # Get the group for this ID
        group = grouped_transcripts.get_group(row['ID'])
        # Use the first occurrence of each value for simplicity
        row['GICS Sector'] = group['GICS Sector'].values[0]
        row['day_date'] = group['day_date_formatted'].values[0]
        row['QTR'] = group['QTR'].values[0]
    return row

# Apply the update_row function to each row in the combined DataFrame
df_combined = df_combined.apply(update_row, axis=1)

# Save the updated DataFrame to a new CSV file
df_combined.to_csv('updated_Qs_and_As_grouped_updated.csv', index=False)

# PART 3
# Date fields check and ensure compatibility

# Function to ensure date parsing and column creation
def ensure_date_compatible(df, date_column, new_column_name='date_compatible'):
    try:
        df[new_column_name] = pd.to_datetime(df[date_column])
        print(
            f"'{date_column}' column successfully parsed and '{new_column_name}' field created.")
    except Exception as e:
        print(f"Error parsing '{date_column}' column: {e}")
    return df


# Load the combined file
# combined_file_path = 'updated_combined_file_updated.csv'
combined_file_path = 'updated_Qs_and_As_grouped_updated.csv'
combined_file = pd.read_csv(combined_file_path)

# Parse the day_date column and create date_compatible field in combined file
combined_file = ensure_date_compatible(combined_file, 'day_date')

# Verify if date_compatible is in datetime format
if pd.api.types.is_datetime64_any_dtype(combined_file['date_compatible']):
    print("'date_compatible' field in combined file is in datetime format.")
else:
    print(
        "'date_compatible' field in combined file is NOT in datetime format.")

# Save the modified combined file
combined_file.to_csv('updated_combined_file_with_compatible_date.csv',
                     index=False)

# Folder containing stock data files
stock_data_folder = 'Stock_Data_Files'

# Get a list of all stock data files
stock_files = [f for f in os.listdir(stock_data_folder) if f.endswith('.csv')]

# Iterate through each stock data file and create date_compatible field
for stock_file in stock_files:
    file_path = os.path.join(stock_data_folder, stock_file)
    stock_df = pd.read_csv(file_path)

    # Parse the Date column and create date_compatible field
    stock_df = ensure_date_compatible(stock_df, 'Date')

    # Verify if date_compatible is in datetime format
    if pd.api.types.is_datetime64_any_dtype(stock_df['date_compatible']):
        print(
            f"'date_compatible' field in {stock_file} is in datetime format.")
    else:
        print(
            f"'date_compatible' field in {stock_file} is NOT in datetime format.")

    # Save the modified stock file
    stock_df.to_csv(file_path, index=False)

print(
    "All files have been updated with 'date_compatible' fields and verified for datetime format.")

# PART 4
# update price change columns in 'updated_combined_file_with_compatible_date.csv’


# Load the combined file
combined_file_path = 'updated_combined_file_with_compatible_date.csv'
combined_df = pd.read_csv(combined_file_path)

# Define the folder containing stock data files
stock_data_folder = 'Stock_Data_Files'

# Function to calculate the fractional difference
def calculate_fractional_difference(stock_df, ec_date, days):
    try:
        # Convert date columns to datetime
        stock_df['date_compatible'] = pd.to_datetime(stock_df['date_compatible'])
        ec_date = pd.to_datetime(ec_date)

        # Check if the earnings call date is in the stock data
        if ec_date not in stock_df['date_compatible'].values:
            return 'date_not_found'

        # Get the index of the earnings call date
        ec_index = stock_df[stock_df['date_compatible'] == ec_date].index[0]

        # Get the close prices for the specified days before and after
        before_df = stock_df.iloc[ec_index - days:ec_index]
        after_df = stock_df.iloc[ec_index + 1:ec_index + 1 + days]

        # Check if there are enough days before and after the EC date
        if len(before_df) < days or len(after_df) < days:
            return 'date_not_found'

        # Calculate the average close prices
        avg_before = before_df['Close'].mean()
        avg_after = after_df['Close'].mean()

        # Calculate the fractional difference
        fractional_diff = (avg_after - avg_before) / avg_before
        return round(fractional_diff, 3)
    except Exception as e:
        return 'date_not_found'

# Iterate over each row in the combined file
for idx, row in combined_df.iterrows():
    ticker = row['Ticker']
    ec_date = row['date_compatible']

    # Construct the file path for the stock data file
    stock_file_path = os.path.join(stock_data_folder, f'{ticker}.csv')

    # Check if the stock data file exists
    if not os.path.exists(stock_file_path):
        combined_df.at[idx, 'price_chng_1day'] = 'date_not_found'
        combined_df.at[idx, 'price_chng_2day'] = 'date_not_found'
        combined_df.at[idx, 'price_chng_5day'] = 'date_not_found'
        continue

    # Load the stock data file
    stock_df = pd.read_csv(stock_file_path)

    # Calculate the fractional difference for 1-day, 2-day, and 5-day changes
    combined_df.at[idx, 'price_chng_1day'] = calculate_fractional_difference(stock_df, ec_date, 1)
    combined_df.at[idx, 'price_chng_2day'] = calculate_fractional_difference(stock_df, ec_date, 2)
    combined_df.at[idx, 'price_chng_5day'] = calculate_fractional_difference(stock_df, ec_date, 5)

# Save the updated combined file
combined_df.to_csv(combined_file_path, index=False)


# PART 5
#  Update tone in updated_combined_file_with_compatible_date.csv

# Load the CSV file into a DataFrame
df = pd.read_csv('updated_combined_file_with_compatible_date.csv')

# Calculate the new 'tone' values
# df['tone'] = (df['count of +ve'] - df['count of -ve']) / (df['count of +ve'] + df['count of -ve'])
# BH 17Jul 20.16
df['tone'] = (df['sum of +ve'] - df['sum of -ve']) / (df['sum of +ve'] + df['sum of -ve'])

# Save the updated DataFrame back to a CSV file
df.to_csv('updated_combined_file_with_compatible_date.csv', index=False)













