import pandas as pd
from IPython.display import display

# Load the dataset
df = pd.read_csv("C:/Users/tomas/OneDrive/BYUIdaho/DS250-homework/StarWars.csv", encoding='latin1', skiprows=1)

# Check raw column names
print("Raw column names from CSV:", df.columns.tolist())

# Define renaming dictionary based on your file's actual column names
new_names = {
    'Unnamed: 0': 'respondent_id',
    'Response': 'seen_any_film',
    'Response.1': 'sw_fan',
    'Star Wars: Episode I  The Phantom Menace': 'seen_episode_1',
    'Star Wars: Episode II  Attack of the Clones': 'seen_episode_2',
    'Star Wars: Episode III  Revenge of the Sith': 'seen_episode_3',
    'Star Wars: Episode IV  A New Hope': 'seen_episode_4',
    'Star Wars: Episode V The Empire Strikes Back': 'seen_episode_5',
    'Star Wars: Episode VI Return of the Jedi': 'seen_episode_6',
    'Star Wars: Episode I  The Phantom Menace.1': 'rank_episode_1',
    'Star Wars: Episode II  Attack of the Clones.1': 'rank_episode_2',
    'Star Wars: Episode III  Revenge of the Sith.1': 'rank_episode_3',
    'Star Wars: Episode IV  A New Hope.1': 'rank_episode_4',
    'Star Wars: Episode V The Empire Strikes Back.1': 'rank_episode_5',
    'Star Wars: Episode VI Return of the Jedi.1': 'rank_episode_6',
    'Han Solo': 'favor_han_solo',
    'Luke Skywalker': 'favor_luke_skywalker',
    'Princess Leia Organa': 'favor_leia',
    'Anakin Skywalker': 'favor_anakin',
    'Obi Wan Kenobi': 'favor_obi_wan',
    'Emperor Palpatine': 'favor_emperor',
    'Darth Vader': 'favor_darth_vader',
    'Lando Calrissian': 'favor_lando',
    'Boba Fett': 'favor_boba_fett',
    'C-3P0': 'favor_c3po',
    'R2 D2': 'favor_r2d2',
    'Jar Jar Binks': 'favor_jar_jar',
    'Padme Amidala': 'favor_padme',
    'Yoda': 'favor_yoda',
    'Response.2': 'shot_first',
    'Response.3': 'know_expanded',
    'Response.4': 'fan_expanded',
    'Response.5': 'trek_fan',
    'Response.6': 'gender',
    'Response.7': 'age',
    'Response.8': 'income',
    'Response.9': 'education',
    'Response.10': 'location'
}

# Create a DataFrame to show old vs. new names
name_mapping_df = pd.DataFrame(list(new_names.items()), columns=['Original Name', 'New Name'])
display("Column name mapping (old vs. new):", name_mapping_df)

# Apply renaming
df = df.rename(columns=new_names)

# Verify all expected columns are present
expected_cols = ['respondent_id', 'seen_any_film', 'sw_fan', 'age', 'education', 'income', 'location']
missing_cols = [col for col in expected_cols if col not in df.columns]
if missing_cols:
    print("Warning: Missing columns after renaming:", missing_cols)
else:
    print("All expected columns present after renaming.")

# Save a copy for Task 3
df_original = df.copy()

# Display columns after renaming
display("Columns after renaming:", pd.DataFrame(df.columns.tolist(), columns=['Column Names']))
display("First few rows of raw data:", df.head())

from IPython.display import display

# Define film columns
film_columns = ['seen_episode_1', 'seen_episode_2', 'seen_episode_3', 
                'seen_episode_4', 'seen_episode_5', 'seen_episode_6']

# Start with renamed df
display_table = df[['respondent_id'] + film_columns].copy()

# a. Filter the dataset to respondents that have seen at least one film
print("### a. Filter the dataset to respondents that have seen at least one film")
display("Rows before filtering:", df.shape)
df = df[df[film_columns].notna().any(axis=1)].copy()
display_table = display_table[display_table[film_columns].notna().any(axis=1)].copy()
display("Rows after filtering:", df.shape)
display("After filtering (sample):", display_table.head())

# b. Create a new column that converts the age ranges to a single number
print("### b. Create a new column that converts the age ranges to a single number")
display("Unique values in 'age' before mapping:", df['age'].unique().tolist())
age_map = {'18-29': 23.5, '30-44': 37, '45-60': 52.5, '> 60': 65}
display("Age mapping: 23.5 = '18-29', 37 = '30-44', 52.5 = '45-60', 65 = '> 60' (midpoints of ranges)")
df['age_numeric'] = df['age'].str.strip().map(age_map)
display("NaN count in age_numeric before fillna:", df['age_numeric'].isna().sum())
df['age_numeric'] = df['age_numeric'].fillna(df['age_numeric'].median())
display("NaN count in age_numeric after fillna:", df['age_numeric'].isna().sum())
display_table = df[['respondent_id', 'age_numeric']].copy()
df.drop(columns=['age'], inplace=True)
display("After age conversion (sample):", display_table.head())

# c. Create a new column that converts the education groupings to a single number
print("### c. Create a new column that converts the education groupings to a single number")
display("Unique values in 'education' before mapping:", df['education'].unique().tolist())
education_map = {
    'Less than high school degree': 0, 'High school degree': 1,
    'Some college or Associate degree': 2, 'Bachelor degree': 3,
    'Graduate degree': 4
}
display("Education mapping: 0 = 'Less than high school degree', 1 = 'High school degree', 2 = 'Some college or Associate degree', 3 = 'Bachelor degree', 4 = 'Graduate degree'")
df['education_numeric'] = df['education'].str.strip().map(education_map)
display("NaN count in education_numeric before fillna:", df['education_numeric'].isna().sum())
df['education_numeric'] = df['education_numeric'].fillna(df['education_numeric'].median())
display("NaN count in education_numeric after fillna:", df['education_numeric'].isna().sum())
display_table = df[['respondent_id', 'age_numeric', 'education_numeric']].copy()
df.drop(columns=['education'], inplace=True)
display("After education conversion (sample):", display_table.head())

# d. Create a new column that converts the income ranges to a single number
print("### d. Create a new column that converts the income ranges to a single number")
display("Unique values in 'income' before mapping:", df['income'].unique().tolist())
income_map = {
    '$0 - $24,999': 1, '$25,000 - $49,999': 2, '$50,000 - $99,999': 3,
    '$100,000 - $149,999': 4, '$150,000+': 5
}
display("Income mapping: 1 = '$0 - $24,999', 2 = '$25,000 - $49,999', 3 = '$50,000 - $99,999', 4 = '$100,000 - $149,999', 5 = '$150,000+'")
df['income_numeric'] = df['income'].str.strip().map(income_map)
display("NaN count in income_numeric before fillna:", df['income_numeric'].isna().sum())
df['income_numeric'] = df['income_numeric'].fillna(df['income_numeric'].median())
display("NaN count in income_numeric after fillna:", df['income_numeric'].isna().sum())
display_table = df[['respondent_id', 'age_numeric', 'education_numeric', 'income_numeric']].copy()
df.drop(columns=['income'], inplace=True)
display("After income conversion (sample):", display_table.head())

# e. Create your target column
print("### e. Create your target (also known as 'y' or 'label') column")
df['target'] = df['income_numeric'].apply(lambda x: 1 if x > 2 else 0)
display_table = df[['respondent_id', 'age_numeric', 'education_numeric', 'income_numeric', 'target']].copy()
display("After target creation (sample):", display_table.head())

# Stretch Task 3: Convert location to numeric
print("### Stretch Task 3: Convert location to numeric")
display("Unique values in 'location' before mapping:", df['location'].unique().tolist())
location_map = {
    'Pacific': 1, 'Mountain': 2, 'West South Central': 3, 'West North Central': 4,
    'East North Central': 5, 'South Atlantic': 6, 'Middle Atlantic': 7, 
    'New England': 8, 'East South Central': 9
}
display("Location mapping: 1 = 'Pacific', 2 = 'Mountain', 3 = 'West South Central', 4 = 'West North Central', 5 = 'East North Central', 6 = 'South Atlantic', 7 = 'Middle Atlantic', 8 = 'New England', 9 = 'East South Central'")
df['location_numeric'] = df['location'].str.strip().map(location_map)
display("NaN count in location_numeric before fillna:", df['location_numeric'].isna().sum())
df['location_numeric'] = df['location_numeric'].fillna(df['location_numeric'].median())
display("NaN count in location_numeric after fillna:", df['location_numeric'].isna().sum())
display_table = df[['respondent_id', 'age_numeric', 'education_numeric', 'income_numeric', 'target', 'location_numeric']].copy()
df.drop(columns=['location'], inplace=True)
display("After location conversion (sample):", display_table.head())