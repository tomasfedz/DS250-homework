import pandas as pd
import numpy as np

# Read in data
url = 'https://raw.githubusercontent.com/byuidatascience/data4names/master/data-raw/names_year/names_year.csv'
df = pd.read_csv(url)

# Question 1: How many babies are named 'Oliver' in Utah (UT) for all years?
oliver_utah = df[(df['name'] == 'Oliver')]['UT'].sum()
print(f"Total babies named Oliver in Utah: {oliver_utah}")

# Question 2: Earliest year Felisha was used
felisha_first_year = df[df['name'] == 'Felisha']['year'].min()
print(f"Earliest year Felisha was used: {felisha_first_year}")