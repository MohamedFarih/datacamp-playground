# Import pandas using the alias pd
import pandas as pd

homelessness = pd.read_csv('datasets/homelessness.csv')

# Filter for rows where individuals is greater than 10000
ind_gt_10k = homelessness[homelessness['individuals'] > 10000]

# See the result
print(ind_gt_10k)