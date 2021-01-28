# Using the matplotlib.pyplot interface
import re

# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt

# Create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots()

# Call the show function to show the result
plt.show()

import pandas as pd
seattle_weather = pd.read_csv('data/seattle_weather.csv', delimiter = ",")

seattle_weather.columns = ((seattle_weather.columns.str).replace("^ ","")).str.replace(" $","")
print(seattle_weather['MONTH'])