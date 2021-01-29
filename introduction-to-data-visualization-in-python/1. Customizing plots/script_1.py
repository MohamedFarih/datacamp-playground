import pandas as pd

percent_bachelors_degrees_women_usa = pd.read_csv('datasets/percent-bachelors-degrees-women-usa.csv')

year = percent_bachelors_degrees_women_usa['Year']
physical_sciences = percent_bachelors_degrees_women_usa['Physical Sciences']

computer_science = percent_bachelors_degrees_women_usa['Computer Science']

health = percent_bachelors_degrees_women_usa['Health Professions']

education = percent_bachelors_degrees_women_usa['Education']

# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Plot in blue the % of degrees awarded to women in the Physical Sciences
plt.plot(year, physical_sciences, color='blue')

# Plot in red the % of degrees awarded to women in Computer Science
plt.plot(year, computer_science, color='red')

# Display the plot
plt.show()
