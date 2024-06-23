import pandas as pd

# Load the CSV file
df = pd.read_csv('co-est2023-pop.csv')

# Convert the relevant columns to numeric, assuming they might contain non-numeric characters
df.iloc[:, 5] = pd.to_numeric(df.iloc[:, 5].str.replace(',', ''), errors='coerce')  # Convert 6th column
df.iloc[:, 2] = pd.to_numeric(df.iloc[:, 2].str.replace(',', ''), errors='coerce')
print(df.head())
# Calculating the difference between the population estimates of 2023 and 2020 using column indices
df['Difference'] = df.iloc[:, 5] - df.iloc[:, 2]

# Format the 'Difference' column with commas as thousands separators
df['Difference'] = df['Difference'].apply(lambda x: f"{x:,.0f}")

# Sorting the DataFrame based on the difference, from most positive to most negative
df_sorted = df.sort_values(by='Difference', ascending=False, key=lambda x: x.str.replace(',', '').astype(float))

# Save the sorted DataFrame to a new CSV file
df_sorted.to_csv('sorted_population_difference.csv', index=False)


