import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'C:/Users/tomas/OneDrive/BYU- Idaho/DS250-homework/Other files/names_year.csv'
data = pd.read_csv(file_path)

# Filter data for the name 'Harry'
diego_data = data[data['name'] == 'Diego']

# Group by year to calculate the total usage nationwide for each year
diego_historical = diego_data.groupby('year')['Total'].sum()

# Create the plot with a larger size
plt.figure(figsize=(15, 8))

# Plot the data
plt.plot(diego_historical.index, diego_historical.values, label="Diego", color="purple", linewidth=2)

# Add a vertical line for 1986
plt.axvline(x=1986, color='red', linestyle='--', alpha=0.5, label='1986')

# Calculate and show the percent change 
if 1986 in diego_historical.index and 1986 in diego_historical.index:
    change_1986_2010 = ((diego_historical[1986] - diego_historical[1986]) / diego_historical[1986] * 100)
    plt.annotate(f'Change 1986-2009: {change_1986_2010:.1f}%', 
                xy=(1986, diego_historical[2010]),
                xytext=(10, 30),
                textcoords='offset points',
                bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5))

# Customize the plot
plt.title("Usage of the Name 'Tony' Over Time\nWith 2008 Reference Line", fontsize=16, pad=20)
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