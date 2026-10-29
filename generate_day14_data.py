import pandas as pd, numpy as np
np.random.seed(14)
rng = np.random.default_rng(14)

customers = ['Kamau Stores','Otieno Wholesale','Hassan Traders','Mombasa Fresh','Nakoli Traders','Kilifi Distributors','Aisha Retail','Baraka Supermarket','Coast Mart','Lamu Traders','Nyali Grocers','Likoni Wholesalers','Changamwe Depot','Mariakani Stores','Voi Junction']
products = ['Rice 25kg','Maize Flour 10kg','Cooking Oil 20L','Sugar 50kg','Tea Leaves 5kg','Wheat Flour 10kg']
counties = ['Mombasa','Kilifi','Kwale','Taita Taveta','Lamu']

price_aug = {'Rice 25kg':3200,'Maize Flour 10kg':1450,'Cooking Oil 20L':5200,'Sugar 50kg':5800,'Tea Leaves 5kg':2100,'Wheat Flour 10kg':1500}
price_sep = {'Rice 25kg':3300,'Maize Flour 10kg':1500,'Cooking Oil 20L':5400,'Sugar 50kg':6000,'Tea Leaves 5kg':2200,'Wheat Flour 10kg':1550}

# August - 243 rows with mismatched column names
aug_rows = []
for _ in range(243):
    prod = str(rng.choice(products))
    aug_rows.append([
        f"2024-08-{int(rng.integers(1,29)):02d}",
        str(rng.choice(customers)),
        str(rng.choice(counties)),
        prod,
        int(rng.integers(2,26)),
        price_aug[prod]
    ])

pd.DataFrame(aug_rows, columns=['date','client_name','county','product','qty','unit_price']).to_csv('sales_august.csv', index=False)

# September - 198 rows, 3 customers dormant, 3 growing
active_customers = [c for c in customers if c not in ['Voi Junction','Coast Mart','Likoni Wholesalers']]
sep_rows = []
for _ in range(198):
    cust = str(rng.choice(active_customers))
    prod = str(rng.choice(products))
    qty = int(rng.integers(2,29))
    if cust in ['Kamau Stores','Otieno Wholesale','Hassan Traders']:
        qty = int(qty * 1.4)
    sep_rows.append([
        f"2024-09-{int(rng.integers(1,31)):02d}",
        cust,
        str(rng.choice(counties)),
        prod,
        qty,
        price_sep[prod]
    ])

pd.DataFrame(sep_rows, columns=['date','customer_name','region','product','quantity','price']).to_csv('sales_september.csv', index=False)

print("OK - Created sales_august.csv (243 rows) and sales_september.csv (198 rows)")