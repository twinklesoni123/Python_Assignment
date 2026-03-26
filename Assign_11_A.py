import pandas as pd
import matplotlib.pyplot as plt

# Read dataset
data = pd.read_csv("company_sales_data.csv")

# a) Total profit line plot
plt.figure()
plt.plot(data['month_number'], data['total_profit'])
plt.title("Total Profit of All Months")
plt.xlabel("Month Number")
plt.ylabel("Total Profit")
plt.show()

# b) Multiline plot for all products
plt.figure()
plt.plot(data['month_number'], data['facecream'], label='Face Cream')
plt.plot(data['month_number'], data['facewash'], label='Face Wash')
plt.plot(data['month_number'], data['toothpaste'], label='Toothpaste')
plt.plot(data['month_number'], data['bathingsoap'], label='Bathing Soap')
plt.plot(data['month_number'], data['shampoo'], label='Shampoo')
plt.plot(data['month_number'], data['moisturizer'], label='Moisturizer')

plt.legend()
plt.xlabel("Month Number")
plt.ylabel("Sales")
plt.title("Sales Data of Products")
plt.show()

# c) Bar chart for Face cream and Face wash
plt.figure()

plt.bar(data['month_number'], data['facecream'], label='Face Cream')
plt.bar(data['month_number'], data['facewash'], label='Face Wash')

plt.xlabel("Month Number")
plt.ylabel("Sales")
plt.title("Face Cream and Face Wash Sales")
plt.legend()
plt.show()

# d) Pie chart of total sales
sales_data = [
    data['facecream'].sum(),
    data['facewash'].sum(),
    data['toothpaste'].sum(),
    data['bathingsoap'].sum(),
    data['shampoo'].sum(),
    data['moisturizer'].sum()
]

labels = ['Face Cream', 'Face Wash', 'Toothpaste', 'Bathing Soap', 'Shampoo', 'Moisturizer']

plt.figure()
plt.pie(sales_data, labels=labels, autopct='%1.1f%%')
plt.title("Total Sales of Each Product")
plt.show()
