import pandas as pd # pd is a toolbox for working with tables. We must import it first.
# This is our first table: orders
orders = pd.DataFrame({
    "order_id": [101, 102, 103],         # ID of each order
    "customer_id": [1, 2, 1],            # WHO made the order. This is the link
    "amount_kes": [45000, 28000, 62000]  # How much they paid
})

# This is our second table: customers
customers = pd.DataFrame({
    "customer_id": [1, 2, 3],      # Same column as in orders! This is the COMMON column
    "name": ["Kamau Stores", "Otieno Wholesale", "Hassan Traders"],
    "county": ["Nairobi", "Kisumu", "Mombasa"]
})

# Now we JOIN them using that common column customer_id
merged = pd.merge(orders, customers, on="customer_id", how="inner")
print(merged)
print("\n--- PIVOT TABLE ---")
sales = pd.DataFrame({
    "month": ["Jan", "Jan", "Feb", "Feb"],
    "county": ["Nairobi", "Kisumu", "Nairobi", "Kisumu"],
    "revenue_kes": [145000, 89000, 162000, 95000]
})
pivot = pd.pivot_table(sales, values="revenue_kes", index="county", columns="month", aggfunc="sum")
print(pivot)
print("\n--- BONUS CALCULATION ---")
sales["commission"] = sales["revenue_kes"].apply(lambda x: x * 0.05 if x > 100000 else x * 0.03)
print(sales)