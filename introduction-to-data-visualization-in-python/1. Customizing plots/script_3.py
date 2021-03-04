import pandas as pd

percent_bachelors_degrees_women_usa = pd.read_csv('datasets/percent-bachelors-degrees-women-usa.csv')

year = percent_bachelors_degrees_women_usa['Year']

physical_sciences = percent_bachelors_degrees_women_usa['Physical Sciences']

computer_science = percent_bachelors_degrees_women_usa['Computer Science']

health = percent_bachelors_degrees_women_usa['Health Professions']

education = percent_bachelors_degrees_women_usa['Education']

# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Create a figure with 1x2 subplot and make the left subplot active
plt.subplot(1,2,1)

# Plot in blue the % of degrees awarded to women in the Physical Sciences
plt.plot(year, physical_sciences, color='blue')
plt.title('Physical Sciences')

# Make the right subplot active in the current 1x2 subplot grid
plt.subplot(1,2,2)

# Plot in red the % of degrees awarded to women in Computer Science
plt.plot(year, computer_science, color='red')
plt.title('Computer Science')

# Use plt.tight_layout() to improve the spacing between subplots
plt.tight_layout()
plt.show()
