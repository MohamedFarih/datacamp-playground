# Import packages
import geopandas as gpd
import matplotlib.pyplot as plt

shapefile_path = 'datasets/ServiceDistricts.shp'

# Read in the services district shapefile and look at the first few rows.
service_district = gpd.read_file(shapefile_path)
print(service_district.head())

# Print the contents of the service districts geometry in the first row
# print(service_district.loc[0, 'geometry'])

# Import pandas and matplotlib.pyplot using their customary aliases
import pandas as pd
import matplotlib.pyplot as plt

chickens_path = 'datasets/chickens_data.csv'

# Load the dataset
chickens = pd.read_csv(chickens_path)

# Look at the first few rows of the chickens DataFrame
print(chickens.head())

# Plot the locations of all Nashville chicken permits
plt.scatter(x = chickens.lng, y = chickens.lat)

# Show the plot
plt.show()

# Plot the service district shapefile
service_district.plot(column='Name', legend=True)

# Add the chicken locations
plt.scatter(x=chickens.lng, y=chickens.lat, c = 'black', edgecolor='white')

# Add labels and title
plt.title('Nashville Chicken Permits')
plt.xlabel('longitude')
plt.ylabel('latitude')

# Add grid lines and show the plot
plt.grid(True)
plt.show()