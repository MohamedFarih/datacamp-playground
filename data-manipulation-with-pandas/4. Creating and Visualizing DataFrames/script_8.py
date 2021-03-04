import pandas as pd 

temperatures = pd.read_csv('../datasets/temperatures.csv')

# Index temperatures by country & city
temperatures_ind = temperatures.set_index(['country', 'city'])

# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
rows_to_keep = [('Brazil', 'Rio De Janeiro'), ('Pakistan', 'Lahore')]

# Subset for rows to keep
print(temperatures_ind.loc[rows_to_keep])

# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()

# Get 23rd row, 2nd column (index 22, 1)
print(temperatures.iloc[23, 2])

# Use slicing to get the first 5 rows
print(temperatures.iloc[:5, :])

# Use slicing to get columns 3 to 4
print(temperatures.iloc[:, 2:5])

# Use slicing in both directions at once
print(temperatures.iloc[:5, 2:5])