import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file to check its structure
file_path = 'C:/Users/tomas/OneDrive/BYU- Idaho/DS250-homework/Other files/names_year.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the dataset to understand its structure
data.head()
# Filter data for the name 'Thomas'
thomas_data = data[data['name'] == 'Thomas']

# Extract historical data and 1996 usage
thomas_historical = thomas_data.groupby('year')['Total'].sum()
thomas_1996 = thomas_data[thomas_data['year'] == 1996]['Total'].sum()

# Plot the data
plt.figure(figsize=(12, 6))
plt.plot(thomas_historical.index, thomas_historical.values, label='Historical Usage', color='blue')
plt.axvline(x=1996, color='red', linestyle='--', label=f'1996 Usage: {thomas_1996:.0f}')

# Adding labels and title
plt.title("Usage of the Name 'Thomas' Over Time", fontsize=16)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Total Count", fontsize=12)
plt.legend(fontsize=10)
plt.grid(alpha=0.5)

# Show the chart
plt.tight_layout()
plt.show()
