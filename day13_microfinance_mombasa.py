"""
Mombasa Microfinance Institution - Loan Repayment Statistical Analysis
Day 13 Exercise - 150 fictional loan records
Author: Johnstone Nakoli
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create dataset of 150 loans (fictional)
np.random.seed(13)
n = 150
loan_ids = [f"LN{1000+i}" for i in range(n)]
amounts = np.random.lognormal(mean=np.log(35000), sigma=0.45, size=n).astype(int)
amounts[5] = 185000; amounts[23] = 210000; amounts[77] = 165000
amounts[2] = 2500; amounts[99] = 3200

days_base = 18 + (amounts - amounts.min()) / (amounts.max() - amounts.min()) * 30
days = np.clip((days_base + np.random.normal(0, 4.5, n)).astype(int), 7, 65)
counties = np.random.choice(['Mombasa', 'Kilifi', 'Kwale', 'Taita Taveta', 'Lamu'], size=n, p=[0.55, 0.20, 0.15, 0.07, 0.03])

df = pd.DataFrame({
    'loan_id': loan_ids,
    'amount_kes': amounts,
    'days_to_first_repayment': days,
    'county': counties
})

# 1. Full Statistical Summary
print("=== TYPICAL LOAN AMOUNT ===")
print(df[['amount_kes','days_to_first_repayment']].describe())
print(f"Mean Amount: {df['amount_kes'].mean():.2f} KES")
print(f"Median Amount: {df['amount_kes'].median():.0f} KES")
print(f"Std Dev: {df['amount_kes'].std():.2f}")

# 2. Outliers using IQR method
Q1 = df['amount_kes'].quantile(0.25)
Q3 = df['amount_kes'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5*IQR
upper_bound = Q3 + 1.5*IQR
outliers = df[(df['amount_kes'] < lower_bound) | (df['amount_kes'] > upper_bound)]

print(f"\n=== UNUSUALLY LARGE OR SMALL LOANS (IQR Method) ===")
print(f"Q1={Q1:.0f}, Q3={Q3:.0f}, IQR={IQR:.0f}")
print(f"Normal range: {lower_bound:.0f} - {upper_bound:.0f} KES")
print(f"Found {len(outliers)} outliers:")
print(outliers[['loan_id','amount_kes','days_to_first_repayment','county']])
print(f"Outlier IDs: {', '.join(outliers['loan_id'].tolist())}")

# 3. Correlation between loan size and days to first repayment
corr = df['amount_kes'].corr(df['days_to_first_repayment'])
print(f"\n=== LINK BETWEEN LOAN SIZE AND REPAYMENT TIME ===")
print(f"Correlation: {corr:.3f}")

# One plain sentence for board
board_sentence = f"Larger loans tend to take slightly longer before the first repayment - customers who borrow more need a few extra days to start paying back."
print(f"\nBoard Summary: {board_sentence}")

# 4. Plot histogram
plt.figure(figsize=(9,5))
plt.hist(df['amount_kes'], bins=20, edgecolor='black')
plt.title('Mombasa MFI: Distribution of Loan Amounts (n=150)')
plt.xlabel('Loan Amount (KES)')
plt.ylabel('Number of Loans')
plt.axvline(df['amount_kes'].mean(), color='red', linestyle='--', label=f"Mean {df['amount_kes'].mean():.0f}")
plt.axvline(df['amount_kes'].median(), color='green', linestyle='-', label=f"Median {df['amount_kes'].median():.0f}")
plt.legend()
plt.tight_layout()
plt.savefig('loan_amounts_histogram.png')
plt.show()

# Save to CSV
df.to_csv('mombasa_microfinance_loans.csv', index=False)
print("\nFiles saved: loan_amounts_histogram.png, mombasa_microfinance_loans.csv")