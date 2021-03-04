# Import pandas using the alias pd
import pandas as pd

homelessness = pd.read_csv('datasets/homelessness.csv')

# Select the individuals column
individuals = homelessness['individuals']

# Print the head of the result
print(individuals.head())