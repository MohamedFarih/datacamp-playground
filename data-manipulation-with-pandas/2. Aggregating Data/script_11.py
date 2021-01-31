# Import numpy with the alias np
import numpy as np

# Import pandas using the alias pd
import pandas as pd 

sales = pd.read_csv('datasets/sales_subset.csv')

# Print mean weekly_sales by department and type; fill missing values with 0
print(sales.pivot_table(values="weekly_sales", index='type', columns ='department', fill_value=0))

# Print the mean weekly_sales by department and type; fill missing values with 0s; sum all rows and cols
print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value=0, margins=0))