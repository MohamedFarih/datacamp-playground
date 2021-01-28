# Customizing axis labels and adding titles
import pandas as pd
seattle_weather = pd.read_csv('data/seattle_weather.csv', index_col='DATE')
austin_weather = pd.read_csv('data/austin_weather.csv', index_col='DATE')
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])

# Customize the x-axis label
ax.set_xlabel("Time (months)")

# Customize the y-axis label
ax.set_ylabel("Precipitation (inches)")

# Add the title
ax.set_title("Weather patterns in Austin and Seattle")

# Display the figure
plt.show()