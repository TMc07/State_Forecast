import pandas as pd

# Load the CSV file
df = pd.read_csv('sorted_population_difference.csv')

# List of columns to convert
print(df.columns)

columns_to_convert = ['Base', 'Off_July_20', 'E21', 'E22', 'E23', 'Diff_23-20']


def clean_and_convert(column):
    # Ensure all values are strings, then replace commas and convert to numeric
    return pd.to_numeric(column.astype(str).str.replace(',', ''), errors='coerce')

# Apply the function to the specified columns
for column in columns_to_convert:
    df[column] = clean_and_convert(df[column])
    df[column] = df[column].fillna(0).astype(int)

    


#Going through and making sure that each of the columns are ints that need to be for operations 
df['Base'] = df['Base'].astype(int)
df['Off_July_20'] = df['Off_July_20'].astype(int)
df['E21'] = df['E21'].astype(int)
df['E22'] = df['E22'].astype(int)
df['E23'] = df['E23'].astype(int)
df['Diff_23-20'] = df['Diff_23-20'].astype(int)

print(df.columns)
print(df.head)

df_length = len(df)

print(df["Diff_23-20"].dtype)
print(df["Base"].dtype)
i = 0

for i in df:
    df['percent_change_23over20'] = (df['Diff_23-20'] / df['Base']) * 100


print(df.head)
df.to_csv('added_percent_growth.csv', index=False)