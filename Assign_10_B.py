import pandas as pd

# Create DataFrame for 3 states
data = {
    'State': ['State1', 'State2', 'State3'],
    'Area': [150000, 200000, 180000],  # in sq km
    'Population': [5000000, 8000000, 6000000]
}

df = pd.DataFrame(data)

# a) Complete information
print("\n--- State Information ---")
print(df)

# b) State with largest area
largest_area = df.loc[df['Area'].idxmax()]
print("\nState with Largest Area:")
print(largest_area['State'])

# c) State with largest population
largest_population = df.loc[df['Population'].idxmax()]
print("\nState with Largest Population:")
print(largest_population['State'])

# d) Calculate population density
df['Density'] = df['Population'] / df['Area']

print("\nPopulation Density of States:")
print(df[['State', 'Density']])

# e) State with highest density
highest_density = df.loc[df['Density'].idxmax()]
print("\nState with Highest Population Density:")
print(highest_density['State'])
