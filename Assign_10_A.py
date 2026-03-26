# import pandas as pd

# Read CSV file
df = pd.read_csv("books.csv")

# a) Print complete report
print("\n--- Complete Book Report ---")
print(df)

# b) List books of a given author
author_name = input("\nEnter author name: ")
print(f"\nBooks by {author_name}:")
print(df[df['Author'] == author_name][['Title', 'Price']])

# c) List books by a given publisher
publisher_name = input("\nEnter publisher name: ")
print(f"\nBooks by {publisher_name}:")
print(df[df['Publisher'] == publisher_name][['Title', 'Price']])

# d) Cheapest and costliest book
cheapest = df[df['Price'] == df['Price'].min()]
costliest = df[df['Price'] == df['Price'].max()]

print("\nCheapest Book:")
print(cheapest[['Title', 'Price']])

print("\nCostliest Book:")
print(costliest[['Title', 'Price']])

# e) Sort by year of publication
print("\nBooks sorted by Year:")
print(df.sort_values(by='Year'))
