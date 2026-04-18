import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"D:\DEBDEEP SARKAR\HERITAGE ENGINEERING\6th Semester\Internships and Placements\Sales_data.csv")

# Show first few rows
print("Dataset Preview:")
print(df.head())

# Total Sales by Region
region_sales = df.groupby("Region")["Sales"].sum()
print("\nTotal Sales by Region:")
print(region_sales)

# Total Sales by Category
category_sales = df.groupby("Category")["Sales"].sum()
print("\nTotal Sales by Category:")
print(category_sales)

# Plot: Sales by Region
plt.figure()
region_sales.plot(kind='bar')
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()

# Plot: Sales by Category
plt.figure()
category_sales.plot(kind='bar')
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()
