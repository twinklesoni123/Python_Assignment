import pandas as pd

# Read Excel file
df = pd.read_excel("employee.xlsx")

# a) Employees in Automotive domain
print("\nEmployees in Automotive Domain")
print(df[df['Department'] == 'Automotive'])

# b) Search by Employee ID
emp_id = int(input("Enter Employee ID: "))
print(df[df['Employee ID'] == emp_id])

# c) Developers list
print("\nDevelopers List")
print(df[df['Designation'] == 'Developer'])
