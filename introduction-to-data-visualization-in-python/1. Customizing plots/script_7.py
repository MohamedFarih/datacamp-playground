import pandas as pd

percent_bachelors_degrees_women_usa = pd.read_csv('datasets/percent-bachelors-degrees-women-usa.csv')

year = percent_bachelors_degrees_women_usa['Year']

physical_sciences = percent_bachelors_degrees_women_usa['Physical Sciences']

computer_science = percent_bachelors_degrees_women_usa['Computer Science']

health = percent_bachelors_degrees_women_usa['Health Professions']

education = percent_bachelors_degrees_women_usa['Education']

# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Specify the label 'Computer Science'
plt.plot(year, computer_science, color='red', label='Computer Science') 

# Specify the label 'Physical Sciences' 
plt.plot(year, physical_sciences, color='blue', label='Physical Sciences')

# Add a legend at the lower center
plt.legend(loc='lower center')

# Add axis labels and title
plt.xlabel('Year')
plt.ylabel('Enrollment (%)')
plt.title('Undergraduate enrollment of women')
plt.show()
