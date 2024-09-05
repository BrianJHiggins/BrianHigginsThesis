
# Results Correlation analysis
# requires file 'updated_combined_file_with_compatible_date.csv'

import pandas as pd
from scipy.stats import pearsonr
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Load the data
file_path = 'updated_combined_file_with_compatible_date.csv'
data = pd.read_csv(file_path)

# Ensure numeric data
columns_to_check = ['tone', 'price_chng_5day', 'price_chng_2day',
                    'price_chng_1day']
for column in columns_to_check:
    data[column] = pd.to_numeric(data[column], errors='coerce')

# Drop rows with NaN values in the required columns
data = data.dropna(subset=columns_to_check)


# Function to calculate correlations and return results in a dictionary
def calculate_correlations(filtered_data):
    correlations = {}
    for price_col in ['price_chng_5day', 'price_chng_2day', 'price_chng_1day']:
        corr, p_value = pearsonr(filtered_data['tone'],
                                 filtered_data[price_col])
        correlations[price_col] = {'Pearson Correlation': corr,
                                   'P-value': p_value}
    return correlations


# Function to create and save scatterplots with trend lines
def create_scatterplot(data, x_col, y_col, title, filename):
    plt.figure(figsize=(8, 6))

    # First, plot the scatter plot
    # sns.scatterplot(x=x_col, y=y_col, data=data, color='blue', s=30)
    # sns.set_palette("pastel")
    sns.scatterplot(x=x_col, y=y_col, data=data, s=30)

    # Then, overlay the trend line (without the scatter points to avoid overlap)
    sns.regplot(x=x_col, y=y_col, data=data, scatter=False, color='red')

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
        scatter_file = os.path.join(plot_dir,
                                    f'{section}_{price_col}_scatter.png')
        create_scatterplot(filtered_data, 'tone', price_col,
                           f'{section}: Tone vs {price_col}', scatter_file)
        image_paths.append((section, f'tone_vs_{price_col}', scatter_file))

    # Create and save correlation matrices
    corr_matrix = filtered_data[['tone', 'price_chng_5day', 'price_chng_2day',
                                 'price_chng_1day']].corr()
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
    ('Q', 'price_chng_5day'): [
        results['Q']['price_chng_5day']['Pearson Correlation'],
        results['Q']['price_chng_5day']['P-value']],
    ('Q', 'price_chng_2day'): [
        results['Q']['price_chng_2day']['Pearson Correlation'],
        results['Q']['price_chng_2day']['P-value']],
    ('Q', 'price_chng_1day'): [
        results['Q']['price_chng_1day']['Pearson Correlation'],
        results['Q']['price_chng_1day']['P-value']],
    ('A', 'price_chng_5day'): [
        results['A']['price_chng_5day']['Pearson Correlation'],
        results['A']['price_chng_5day']['P-value']],
    ('A', 'price_chng_2day'): [
        results['A']['price_chng_2day']['Pearson Correlation'],
        results['A']['price_chng_2day']['P-value']],
    ('A', 'price_chng_1day'): [
        results['A']['price_chng_1day']['Pearson Correlation'],
        results['A']['price_chng_1day']['P-value']],
    ('Q&A', 'price_chng_5day'): [
        results['Q&A']['price_chng_5day']['Pearson Correlation'],
        results['Q&A']['price_chng_5day']['P-value']],
    ('Q&A', 'price_chng_2day'): [
        results['Q&A']['price_chng_2day']['Pearson Correlation'],
        results['Q&A']['price_chng_2day']['P-value']],
    ('Q&A', 'price_chng_1day'): [
        results['Q&A']['price_chng_1day']['Pearson Correlation'],
        results['Q&A']['price_chng_1day']['P-value']]
}, index=['Pearson Correlation', 'P-value'])

# Save results to CSV file
result_file = 'Q&A_tone_price_correlation.csv'
result_df.to_csv(result_file)
print(f"Correlation results saved to: {result_file}")  # Debug statement

# Save the image paths to a CSV file
image_df = pd.DataFrame(image_paths,
                        columns=['Section', 'Plot_Type', 'File_Path'])
image_paths_file = 'plots_image_paths.csv'
image_df.to_csv(image_paths_file, index=False)
print(f"Image paths saved to: {image_paths_file}")  # Debug statement

print("Correlation analysis complete. Results and plots saved.")

