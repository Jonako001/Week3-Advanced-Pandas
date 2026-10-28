import pandas as pd

# --- INPUT FILE 1: Daily Milk Collection (collection.csv) ---
collection_data = {
    "farmer_name": [
        "Donald Ekuwom", "Mcdennis Ebei", "Lomoe Ejore", "Dominic Lojore",
        "Sabina Akai", "Ipasa Maraka", "Stephen Erupe", "Chebet Lagat", 
        "Daisy Emus", "Atieno Odhiambo", "Timothy Ajon", "Ekunoit Moses", 
        "Shown Erupe", "Phoebe Ekai", "Tom Ejore", "Ekai James"
    ],
    "date": [
        "2026-10-26", "2026-10-12", "2026-10-11", "2026-10-09",
        "2026-10-02", "2026-10-05", "2026-10-15", "2026-10-03",
        "2026-10-16", "2026-10-25", "2026-10-19", "2026-10-14",
        "2026-10-18", "2026-10-20", "2026-10-22", "2026-10-17"
    ],
    "litres": [95, 40, 80, 100, 65, 50, 85, 90, 45, 92, 75, 60,
    80, 65, 50, 45]
}


# --- INPUT FILE 2: Farmer Details (farmers.csv) ---
farmer_data = {
    "farmer_name": [
        "Donald Ekuwom", "Mcdennis Ebei", "Lomoe Ejore", "Dominic Lojore",
        "Sabina Akai", "Ipasa Maraka", "Shown Erupe", "Chebet Lagat", 
        "Daisy Emus", "Atieno Odhiambo", "Timothy Ajon", "Ekunoit Moses",
        "Stephen Erupe", "Ekai James", "Tom Ejore", "Phoebe Ekai"
    ],
    "zone": [
        "Kerio", "Kalokol", "Napetet", "Kalokol",
        "Kerio", "Napetet", "Kalokol", "Kerio", 
        "Napetet", "Kerio", "Kalokol", "Napetet",
        "Kalokol", "Napetet", "Kerio", "Kerio"
    ],
    "rate_per_litre": [52, 50, 51, 50, 54, 52, 55, 53, 52, 50, 53, 52, 54, 52, 55, 53]
}


collection_df = pd.DataFrame(collection_data)
farmers_df = pd.DataFrame(farmer_data)

# Merge on farmer name

merged = pd.merge(collection_df, farmers_df, on="farmer_name", how="inner")
merged["payout_kes"] = merged["litres"] * merged["rate_per_litre"]
merged["date"] = pd.to_datetime(merged["date"])
this_month = merged[merged["date"].dt.month == 10]


# Summary
total_litres = this_month.groupby("zone")["litres"].sum().reset_index()
total_payout = this_month.groupby("zone")["payout_kes"].sum().reset_index()
farmer_totals = this_month.groupby(["zone", "farmer_name"])["litres"].sum().reset_index()
top_farmers = farmer_totals.loc[farmer_totals.groupby("zone")["litres"].idxmax()]
top_farmers = top_farmers.rename(columns={"farmer_name": "top_farmer", "litres": "top_farmer_litres"})



summary = pd.merge(total_litres, total_payout, on="zone")
summary = pd.merge(summary, top_farmers, on="zone")
summary = summary.rename(columns={"litres": "total_litres_this_month", "payout_kes": "total_payout_kes"})
summary = summary[["zone", "total_litres_this_month", "total_payout_kes", "top_farmer", "top_farmer_litres"]].sort_values(by="total_litres_this_month", ascending=False)


print("\n=== ATURKAN DAIRY CO-OP - MONTHLY SUMMARY (OCTOBER 2026) ===")
print(summary.to_string(index=False))