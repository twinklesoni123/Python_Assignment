import pandas as pd
import matplotlib.pyplot as plt

# Read dataset
data = pd.read_csv("company_sales_data.csv")

# Multiline Plot for all products
plt.figure()

plt.plot(data['month_number'], data['facecream'], label='Face Cream')
plt.plot(data['month_number'], data['facewash'], label='Face Wash')
plt.plot(data['month_number'], data['toothpaste'], label='Toothpaste')
plt.plot(data['month_number'], data['bathingsoap'], label='Bathing Soap')
plt.plot(data['month_number'], data['shampoo'], label='Shampoo')
plt.plot(data['month_number'], data['moisturizer'], label='Moisturizer')

plt.xlabel("Month Number")
plt.ylabel("Sales Units")
plt.title("Sales Data of All Products")

plt.legend()
plt.show()
