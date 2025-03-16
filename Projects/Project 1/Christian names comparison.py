import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'C:/Users/tomas/OneDrive/BYU- Idaho/DS250-homework/Other files/names_year.csv'
data = pd.read_csv(file_path)

# Create a list of names to analyze
names_to_analyze = ['Mary', 'Martha', 'Peter', 'Paul']

# Create figure with larger size for better readability
plt.figure(figsize=(15, 8))

# Plot each name
for name in names_to_analyze:
    # Filter data for each name
    name_data = data[data['name'] == name]
    
    # Group by year and sum the total usage
    historical_usage = name_data.groupby('year')['Total'].sum()
    
    # Filter for years between 1920 and 2000
    historical_usage = historical_usage[(historical_usage.index >= 1920) & (historical_usage.index <= 2000)]
    
    # Plot the data
    plt.plot(historical_usage.index, historical_usage.values, label=name, linewidth=2)

# Customize the plot
plt.title("Usage of Christian Names (1920-2000)", fontsize=16, pad=20)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Total Count", fontsize=12)
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)

# Add thousand separator to y-axis
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: format(int(x), ',')))

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Show the plot
plt.show()