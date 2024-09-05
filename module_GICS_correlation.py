
# tone - price change correlation analysis by GICS
# produces scatter plots and correlation matrices

import pandas as pd
from scipy.stats import pearsonr
import numpy as np

# Load the data
file_path = 'updated_combined_file_with_compatible_date.csv'
df = pd.read_csv(file_path)

# Ensure the required columns are numeric
columns_to_check = ['tone', 'price_chng_5day', 'price_chng_2day',
                    'price_chng_1day']
df[columns_to_check] = df[columns_to_check].apply(pd.to_numeric,
                                                  errors='coerce')

# Initialize a list to store the results
results = []


# Function to calculate the Pearson correlation and store the result
def calculate_and_store_correlation(df, section_value, gics_sector, results):
    filtered_df = df[(df['Call_Section'] == section_value) & (
                df['GICS Sector'] == gics_sector)]

    # Drop rows with NaN or inf values in the relevant columns
    filtered_df = filtered_df.replace([np.inf, -np.inf], np.nan).dropna(
        subset=['tone', 'price_chng_5day', 'price_chng_2day',
                'price_chng_1day'])

    # Ensure there are enough data points to compute correlation
    if len(filtered_df) > 1:
        for price_column in ['price_chng_5day', 'price_chng_2day',
                             'price_chng_1day']:
            correlation, p_value = pearsonr(filtered_df['tone'],
                                            filtered_df[price_column])
            results.append({
                'Call_Section': section_value,
                'GICS Sector': gics_sector,
                'Tone_vs': price_column,
                'Correlation': correlation,
                'P-Value': p_value
            })
    else:
        for price_column in ['price_chng_5day', 'price_chng_2day',
                             'price_chng_1day']:
            results.append({
                'Call_Section': section_value,
                'GICS Sector': gics_sector,
                'Tone_vs': price_column,
                'Correlation': np.nan,
                'P-Value': np.nan
            })


# Get unique GICS sectors
gics_sectors = df['GICS Sector'].unique()

# Calculate correlations for 'Q' and 'A' for each GICS sector
for gics_sector in gics_sectors:
    calculate_and_store_correlation(df, 'Q', gics_sector, results)
    calculate_and_store_correlation(df, 'A', gics_sector, results)

# Convert results to a DataFrame
results_df = pd.DataFrame(results)

# Save the results to a CSV file
output_file = 'Q&A_tone_price_correlation_by_GICS.csv'
results_df.to_csv(output_file, index=False)

results_df

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = 'updated_combined_file_with_compatible_date.csv'
df = pd.read_csv(file_path)

# Ensure the required columns are numeric
columns_to_check = ['tone', 'price_chng_5day', 'price_chng_2day',
                    'price_chng_1day']
df[columns_to_check] = df[columns_to_check].apply(pd.to_numeric,
                                                  errors='coerce')

# Drop rows with NaN or inf values in the relevant columns
df = df.replace([np.inf, -np.inf], np.nan).dropna(
    subset=['tone', 'price_chng_5day', 'price_chng_2day', 'price_chng_1day'])


# Define a function to plot trend lines
def plot_trend_lines(call_section, price_column):
    plt.figure(figsize=(10, 6))
    for gics_sector in df['GICS Sector'].unique():
        sector_df = df[(df['Call_Section'] == call_section) & (
                    df['GICS Sector'] == gics_sector)]

        if len(sector_df) > 1:  # Ensure there are enough data points
            # Scatter plot
            sns.regplot(x='tone', y=price_column, data=sector_df,
                        label=gics_sector, ci=None)

    plt.title(f'Trend Line for {call_section} - {price_column}')
    plt.xlabel('Tone')
    plt.ylabel(price_column)
    plt.legend(title='GICS Sector')
    plt.grid(True)
    plt.show()


# Plot trend lines for 'Q' and 'A' for each price change column
for call_section in ['Q', 'A']:
    for price_column in ['price_chng_5day', 'price_chng_2day',
                         'price_chng_1day']:
        plot_trend_lines(call_section, price_column)
