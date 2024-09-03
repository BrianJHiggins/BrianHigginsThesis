
"""
 module 3.1
 Processes the series of output files (all contained in folder 'FinBERT output files combined') from FinBERT
 First: Lines 12 - 52 are required to recombine the contents of unzipped folders
 'FinBERT output files combined Part1' and FinBERT output files combined Part2
 when downloaded from GitHUB
"""
# Recombine contents of two folders

# import os
import shutil
import pandas as pd
import os


# Define the paths for the source folders and the destination folder
part1_folder = 'FinBERT output files combined Part1'
part2_folder = 'FinBERT output files combined Part2'
combined_folder = 'FinBERT output files combined'

# Remove the combined folder if it already exists
if os.path.exists(combined_folder):
    shutil.rmtree(combined_folder)
    print(f"Deleted existing folder: {combined_folder}")

# Create the combined folder
os.makedirs(combined_folder)
print(f"Created new folder: {combined_folder}")


# Function to copy files from one folder to another
def copy_files(source_folder, destination_folder):
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            source_file = os.path.join(root, file)
            destination_file = os.path.join(destination_folder, file)

            # If the file already exists in the destination, handle it (e.g., by renaming or overwriting)
            if os.path.exists(destination_file):
                # Example: rename the file by appending a suffix
                filename, extension = os.path.splitext(file)
                destination_file = os.path.join(destination_folder,
                                                f"{filename}_copy{extension}")

            shutil.copy2(source_file, destination_file)
            print(f"Copied {source_file} to {destination_file}")


# Copy files from Part1 and Part2 folders to the combined folder
copy_files(part1_folder, combined_folder)
copy_files(part2_folder, combined_folder)

print("All files have been combined successfully!")


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


