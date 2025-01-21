import pandas as pd

# URL of the CSV file
url = 'https://github.com/byuidatascience/data4names/raw/master/data-raw/names_year/names_year.csv'

# Read the CSV file from the URL
data = pd.read_csv(url)

# Save the CSV file to your local machine
data.to_csv('names_year.csv', index=False)

print("File saved as 'names_year.csv'")
