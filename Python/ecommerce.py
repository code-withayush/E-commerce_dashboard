
# IMPORT LIBRARIES
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# LOAD DATA
df = pd.read_csv("../Data/ecommerce_sales_dataset.csv")

print(df.head())
print(df.info())
print(df.describe())


# DATA CLEANING

print("Missing values:\n", df.isna().sum())
df = df.fillna(0)

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)


# ANALYSIS


# 1 Total Revenue by Product Category
category_revenue = (
    df.groupby("Product_Category")["Total amount"]
    .sum()
    .reset_index()
)

plt.figure(figsize=(10,6))
sns.barplot(data=category_revenue, x="Product_Category", y="Total amount")
plt.title("Total Revenue by Product Category")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

# 2 Top 10 Products by Quantity Sold
top_products = (
    df.groupby("Product_Name")["Quantity"]
    .sum()
    .reset_index()
    .sort_values(by="Quantity", ascending=False)
    .head(10)
)

plt.figure(figsize=(10,6))
sns.barplot(data=top_products, x="Quantity", y="Product_Name")
plt.title("Top 10 Best Selling Products")
plt.tight_layout()
plt.show()

# 3 Revenue Trend Over Time
daily_revenue = (
    df.groupby("Date")["Total amount"]
    .sum()
    .reset_index()
)

plt.figure(figsize=(12,6))
sns.lineplot(data=daily_revenue, x="Date", y="Total amount")
plt.title("Revenue Trend Over Time")
plt.xticks(rotation=40)
plt.tight_layout()
plt.show()

# 4 City-wise Revenue
city_revenue = (
    df.groupby("City")["Total amount"]
    .sum()
    .reset_index()
)

plt.figure(figsize=(8,5))
sns.barplot(data=city_revenue, x="City", y="Total amount")
plt.title("Revenue by City")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()


# SAVE CLEANED DATA

df.to_csv("../Data/ecommerce_cleaned.csv", index=False)
print("Cleaned dataset saved for Power BI")
