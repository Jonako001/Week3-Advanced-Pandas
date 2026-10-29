"""
Day 14: Multi-Dataset Analysis - Mombasa Distributor
Author: Johnstone Nakoli
"""
import pandas as pd

# STEP 1: Load
august = pd.read_csv("sales_august.csv")
september = pd.read_csv("sales_september.csv")
print("August columns:", august.columns.tolist())
print("September columns:", september.columns.tolist())
print(f"August: {len(august)} rows | September: {len(september)} rows")

# STEP 2: Resolve mismatches - rename to standard format
august = august.rename(columns={
    "client_name": "customer",
    "county": "region",
    "qty": "quantity",
    "unit_price": "price"
})
september = september.rename(columns={
    "customer_name": "customer"
})
august["month"] = "August"
september["month"] = "September"

# STEP 3: Merge - vertical stack (concat)
combined = pd.concat([august, september], ignore_index=True)
combined["revenue"] = combined["quantity"] * combined["price"]
print(f"Combined: {len(combined)} rows")
print(combined.groupby("month")["quantity"].sum())

# STEP 4: Analysis across time
monthly_revenue = combined.groupby(["month","customer"], as_index=False).agg(
    total_revenue=("revenue","sum")
)

# Pivot with safety check
pivot = monthly_revenue.pivot_table(index="customer", columns="month", values="total_revenue", fill_value=0)

# Make sure both months exist even if data is missing
for m in ["August","September"]:
    if m not in pivot.columns:
        pivot[m] = 0

print("\nPivot columns found:", pivot.columns.tolist())

pivot["growth"] = pivot["September"] - pivot["August"]
# Avoid divide by zero
pivot["pct_change"] = pivot.apply(lambda r: ((r["September"]-r["August"])/r["August"]*100) if r["August"]!=0 else 0, axis=1).round(1)

top_growers = pivot.sort_values("pct_change", ascending=False).head(5)
print("\nTop 5 Growing Customers:")
print(top_growers)

overall = combined.groupby("month")["revenue"].sum()
for m in ["August","September"]:
    if m not in overall.index:
        overall[m] = 0

print("\nOverall Revenue by Month:")
print(overall)

# STEP 5: Findings
dormant_customers = set(august["customer"].unique()) - set(september["customer"].unique())
lost_rev = monthly_revenue[(monthly_revenue["customer"].isin(dormant_customers)) & (monthly_revenue["month"]=="August")]["total_revenue"].sum()

print("\n=== THREE FINDINGS FOR CLIENT ===")
fall_pct = ((overall['September']-overall['August'])/overall['August']*100) if overall['August']!=0 else 0
print(f"Finding 1: Overall revenue fell {fall_pct:.1f}% from August (KES {overall['August']:,.0f}) to September (KES {overall['September']:,.0f}). Needs investigation.")
print(f"Finding 2: Top growers are {', '.join(top_growers.index[:3])} with strong growth despite overall decline. Decline came from smaller accounts, not top accounts.")
print(f"Finding 3: {len(dormant_customers)} customers ({', '.join(dormant_customers) if dormant_customers else 'None'}) placed no orders in September. They represent KES {lost_rev:,.0f} in lost repeat revenue and should be contacted directly.")