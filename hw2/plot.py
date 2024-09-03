import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
dataset_5 = pd.read_csv("results_5_50.csv", encoding='latin1')

# Print the cleaned data to verify
print(dataset_5.head())

# Determine the maximum and minimum values for the y-axis
max_v5 = dataset_5['V5'].max()
min_v5 = dataset_5['V5'].min()
max_v50 = dataset_5['V50'].max()
min_v50 = dataset_5['V50'].min()

# Set the y-axis limits
y_min = min(min_v5, min_v50)
y_max = max(max_v5, max_v50)

# Create the boxplot
ax = sns.boxplot(data=dataset_5[['V5', 'V50']], palette="Set2")

# Adjust the scale of the y-axis
plt.ylim(y_min, y_max)

# Show the plot
plt.show()