import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file to check its structure
file_path = 'C:/Users/tomas/OneDrive/BYU- Idaho/DS250-homework/Other files/names_year.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the dataset to understand its structure
data.head()


# Filter data for the name 'Brittany'
brittany_data = data[data['name'] == 'Brittany']

# Group by year to calculate the total usage nationwide for each year
brittany_historical = brittany_data.groupby('year')['Total'].sum()

# Plot the data
plt.figure(figsize=(12, 6))
plt.plot(brittany_historical.index, brittany_historical.values, label="Nationwide Usage", color="purple")

# Adding labels, title, and grid
plt.title("Nationwide Popularity of the Name 'Brittany' Over Time", fontsize=16)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Total Count", fontsize=12)
plt.legend(fontsize=10)
plt.grid(alpha=0.5)

# Show the chart
plt.tight_layout()
plt.show()

