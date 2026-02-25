import pandas as pd

# Load in data
df = pd.read_csv('data/tourism_data.csv')

# Select relevant columns
df = df[['Year', 'Country', 'ISO3', 'GDP_Growth_Percent', 'Tourism_Revenue']]

# Add cumulitive tourism revenue column
df['Cumulative_Tourism_Revenue'] = df.groupby('Country')['Tourism_Revenue'].cumsum()

# Save in data folder
df.to_csv('data/transformed_tourism_data.csv')
