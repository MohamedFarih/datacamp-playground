# Import pandas using the alias pd
import pandas as pd

homelessness = pd.read_csv('datasets/homelessness.csv')

# Sort homelessness by individual
homelessness_ind = homelessness.sort_values('individuals')

# Print the top few rows
print(homelessness_ind.head())