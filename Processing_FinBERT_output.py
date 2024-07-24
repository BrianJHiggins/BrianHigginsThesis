
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






# # # ChatGPT Update tone in updated_combined_file_with_compatible_date.csv 14Jul21.25
# import pandas as pd
#
# # Load the CSV file into a DataFrame
# df = pd.read_csv('updated_combined_file_with_compatible_date.csv')
#
# # Calculate the new 'tone' values
# # df['tone'] = (df['count of +ve'] - df['count of -ve']) / (df['count of +ve'] + df['count of -ve'])
# # BH 17Jul 20.16
# df['tone'] = (df['sum of +ve'] - df['sum of -ve']) / (df['sum of +ve'] + df['sum of -ve'])
#
# # Save the updated DataFrame back to a CSV file
# df.to_csv('updated_combined_file_with_compatible_date.csv', index=False)
#
# #All works to here BH 19 Jul 09.45





# Correlation analysis
import pandas as pd
from scipy.stats import pearsonr
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Load the data
file_path = 'updated_combined_file_with_compatible_date.csv'
data = pd.read_csv(file_path)

# Ensure numeric data
columns_to_check = ['tone', 'price_chng_5day', 'price_chng_2day', 'price_chng_1day']
for column in columns_to_check:
    data[column] = pd.to_numeric(data[column], errors='coerce')

# Drop rows with NaN values in the required columns
data = data.dropna(subset=columns_to_check)

# Function to calculate correlations and return results in a dictionary
def calculate_correlations(filtered_data):
    correlations = {}
    for price_col in ['price_chng_5day', 'price_chng_2day', 'price_chng_1day']:
        corr, p_value = pearsonr(filtered_data['tone'], filtered_data[price_col])
        correlations[price_col] = {'Pearson Correlation': corr, 'P-value': p_value}
    return correlations

# Function to create and save scatterplots
def create_scatterplot(data, x_col, y_col, title, filename):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=x_col, y=y_col, data=data)
    plt.title(title)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.savefig(filename)
    plt.close()
    print(f"Scatter plot saved: {filename}")  # Debug statement

# Directory to save plots
plot_dir = 'plots'
if not os.path.exists(plot_dir):
    os.makedirs(plot_dir)
    print(f"Created directory: {plot_dir}")  # Debug statement
else:
    print(f"Directory already exists: {plot_dir}")  # Debug statement

# Filter data by Call_Section and calculate correlations
results = {}
image_paths = []

for section in ['Q', 'A', 'Q&A']:
    if section == 'Q&A':
        filtered_data = data[data['Call_Section'].isin(['Q', 'A'])]
    else:
        filtered_data = data[data['Call_Section'] == section]

    results[section] = calculate_correlations(filtered_data)

    # Create and save scatterplots
    for price_col in ['price_chng_5day', 'price_chng_2day', 'price_chng_1day']:
        scatter_file = os.path.join(plot_dir, f'{section}_{price_col}_scatter.png')
        create_scatterplot(filtered_data, 'tone', price_col, f'{section}: Tone vs {price_col}', scatter_file)
        image_paths.append((section, f'tone_vs_{price_col}', scatter_file))

    # Create and save correlation matrices
    corr_matrix = filtered_data[['tone', 'price_chng_5day', 'price_chng_2day', 'price_chng_1day']].corr()
    heatmap_file = os.path.join(plot_dir, f'{section}_correlation_matrix.png')
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title(f'{section} Correlation Matrix')
    plt.savefig(heatmap_file)
    plt.close()
    print(f"Correlation matrix saved: {heatmap_file}")  # Debug statement
    image_paths.append((section, 'correlation_matrix', heatmap_file))

# Convert results to a DataFrame
result_df = pd.DataFrame({
    ('Q', 'price_chng_5day'): [results['Q']['price_chng_5day']['Pearson Correlation'], results['Q']['price_chng_5day']['P-value']],
    ('Q', 'price_chng_2day'): [results['Q']['price_chng_2day']['Pearson Correlation'], results['Q']['price_chng_2day']['P-value']],
    ('Q', 'price_chng_1day'): [results['Q']['price_chng_1day']['Pearson Correlation'], results['Q']['price_chng_1day']['P-value']],
    ('A', 'price_chng_5day'): [results['A']['price_chng_5day']['Pearson Correlation'], results['A']['price_chng_5day']['P-value']],
    ('A', 'price_chng_2day'): [results['A']['price_chng_2day']['Pearson Correlation'], results['A']['price_chng_2day']['P-value']],
    ('A', 'price_chng_1day'): [results['A']['price_chng_1day']['Pearson Correlation'], results['A']['price_chng_1day']['P-value']],
    ('Q&A', 'price_chng_5day'): [results['Q&A']['price_chng_5day']['Pearson Correlation'], results['Q&A']['price_chng_5day']['P-value']],
    ('Q&A', 'price_chng_2day'): [results['Q&A']['price_chng_2day']['Pearson Correlation'], results['Q&A']['price_chng_2day']['P-value']],
    ('Q&A', 'price_chng_1day'): [results['Q&A']['price_chng_1day']['Pearson Correlation'], results['Q&A']['price_chng_1day']['P-value']]
}, index=['Pearson Correlation', 'P-value'])

# Save results to CSV file
result_file = 'Q&A_tone_price_correlation.csv'
result_df.to_csv(result_file)
print(f"Correlation results saved to: {result_file}")  # Debug statement

# Save the image paths to a CSV file
image_df = pd.DataFrame(image_paths, columns=['Section', 'Plot_Type', 'File_Path'])
image_paths_file = 'plots_image_paths.csv'
image_df.to_csv(image_paths_file, index=False)
print(f"Image paths saved to: {image_paths_file}")  # Debug statement

print("Correlation analysis complete. Results and plots saved.")
