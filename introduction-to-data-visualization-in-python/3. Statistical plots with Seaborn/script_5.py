# Grouping linear regressions by row or column

# Plot linear regressions between 'weight' and 'hp' grouped row-wise by 'origin'
sns.lmplot(data=auto, x='weight', y='hp', hue='origin', row='origin')

# Display the plot
plt.show()
