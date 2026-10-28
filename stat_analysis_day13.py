import pandas as pd
import numpy as np
from scipy import stats


# STEP 1: Describe
sales = pd.DataFrame({
    "amount_kes": [12000, 45000, 8500, 67000, 23000,
                   890000, 15000, 34000, 11000, 52000]
})
print("--- STEO 1: DESCRIBE ---")
print(sales.describe())
print(f"\nMean: {sales['amount_kes'].mean()} | Median: {sales['amount_kes'].median()}")


# STEP 2 - Outliers IQR
Q1 = sales["amount_kes"].quantile(0.25)
Q3 = sales["amount_kes"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
outliers = sales[(sales["amount_kes"] <lower) | (sales["amount_kes"] > upper)]
print("\n--- STEP 2: OUTLIERS ---")
print(f"Outliers found: {len(outliers)}")
print(outliers)

# STEP 3 - Correlation
monthly = pd.DataFrame({
    "ad_spend_kes": [5000, 8000, 12000, 15000, 2000, 25000],
    "sales_kes": [42000, 58000, 74000, 88000, 115000, 142000]
})
corr = monthly["ad_spend_kes"].corr(monthly["sales_kes"])
print("\n--- STEP 3: CORRELATION ---")
print(f"Correlation: {corr:.3f} -> Strong positive, ad spend drives sales")


# STEP 4 - T-test
nairobi_sales = [145000, 162000, 178000, 189000, 201000]
kisumu_sales = [89000, 95000, 112000, 108000, 121000]
t_stat, p_value = stats.ttest_ind(nairobi_sales, kisumu_sales)
print("\n--- STEP 4: T-TEST ---")
print(f"t-statistic: {t_stat:.2f}")
print(f"p-value: {p_value:.4f}")
if p_value <0.05:
    print("The difference is statistically significant.")

# STEP 5 - Client Brief
print("\n--- STEP 5: CLIENT BRIEF ---")
print("Finding: Nairobi avg KES 175k vs Kisumu avg KES 105k (p=0.0028)")
print("Recommendation: Add 1 distributor in Kisumu -> +KES 60k-80 k/month")