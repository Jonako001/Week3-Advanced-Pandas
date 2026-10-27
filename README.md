# Nakuru Dairy Co-op - Monthly Zone Summary

This script merges daily milk collection with farmer details to give the manager a clean monthly report.

### What it does
1.  Merges two DataFrames on `farmer_name`
2.  Calculates `payout_kes = litres * rate_per_litre`
3.  Groups by `zone` to get total litres and total payout
4.  Finds top farmer per zone (most litres)
5.  Prints a client-ready summary table + pivot table

### Two Input Files Needed (in real deployment)
1.  **collection.csv** -> `farmer_name, date, litres`
2.  **farmers.csv** -> `farmer_name, zone, rate_per_litre`

Currently using realistic sample data for 12 farmers across 3 Nakuru zones: Molo, Bahati, Subukia.

### How to run
python day2_nakuru_coop.py
