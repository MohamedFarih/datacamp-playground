# Grouping linear regressions by hue

# Plot a linear regression between 'weight' and 'hp', with a hue of 'origin' and palette of 'Set1'
sns.lmplot(data=auto, x='weight', y='hp', hue='origin', palette='Set1')

# Display the plot
plt.show()
