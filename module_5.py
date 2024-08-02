# MODULE_5
# Processes the series of output files (all in folder 'FinBERT output files combined') from FinBERT

import pandas as pd
import os

# Define the directory containing the CSV files (in the same location as the script)
directory = 'FinBERT output files combined'

# Define the fields to group by
group_fields = ['ID', 'Call_Section']

# Define the fields to sum
sum_fields = ['count of +ve', 'count of -ve', 'count of neutral']

# Define the fields to keep
keep_fields = ['Company_AName', 'Ticker', 'Text']

# Initialize an empty list to store the grouped DataFrames
grouped_dataframes = []

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        # Construct the full file path
        file_path = os.path.join(directory, filename)

        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)

        # Ensure the sum fields are numeric
        for field in sum_fields:
            df[field] = pd.to_numeric(df[field], errors='coerce')

        # Select the necessary fields
        df = df[group_fields + sum_fields + keep_fields]

        # Group the DataFrame by the specified fields and sum the required fields
        grouped_df = df.groupby(group_fields + keep_fields)[sum_fields].sum().reset_index()

        # Append the grouped DataFrame to the list
        grouped_dataframes.append(grouped_df)

# Concatenate all the grouped DataFrames
combined_df = pd.concat(grouped_dataframes)

# Group the combined DataFrame again to ensure proper aggregation
combined_df = combined_df.groupby(group_fields + keep_fields)[sum_fields].sum().reset_index()

# Rename the columns as required
combined_df = combined_df.rename(columns={
    'count of +ve': 'sum of +ve',
    'count of -ve': 'sum of -ve',
    'count of neutral': 'sum of neutral'
})

# Define the output file path
output_file_path = 'combined_file.csv'

# Save the combined DataFrame to a new CSV file in the current working directory
combined_df.to_csv(output_file_path, index=False)

print(f"Grouping and combination of CSV files is complete. Output saved to '{output_file_path}'.")
