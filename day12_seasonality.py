import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# STEP 1: Generate 18 months of realistic daily data (May 2023 - oct 2024)
np.random.seed(42)  # so your chart is reproducible
dates = pd.date_range(start="2023-05-01", end="2024-10-31", freq="D") #549

# Base traffic 250- 350 per day with slow growth trend
base = 280
trend = np.linspace(0, 80, len(dates))  # growing business: +80 customers over 18 months

# Seasonality: Dec high, Feb low
seasonal = []
for d in dates:
    if d.month == 12:
        seasonal.append(120) # Dec holiday rush
    elif d.month == 11:
        seasonal.append(40)  # Nov build-up
    elif d.month == 2:
        seasonal.append(-60)   # Feb low
    elif d.month == 1:
        seasonal.append(-20)  # Jan slow
    elif d.month in [7, 8]:
        seasonal.append(20)   # mid-year slight bump
    else:
        seasonal.append(0)

seasonal = np.array(seasonal)

# Weekend effect + random noise
weekend = np.array([40 if d.weekday() >=5 else 0 for d in dates])  # Sat/Sun higher
noise = np.random.normal(0, 30, len(dates))

transactions = base + trend + seasonal + weekend + noise
transactions = np.maximum(transactions, 150).astype(int) # never below 150


df = pd.DataFrame({"date": dates, "transactions": transactions})
df = df.set_index("date")

# STEP 2: Monthly totals + 30-day rolling average
monthly = df["transactions"]. resample("ME").sum()  # monthly total transactions
rolling_30d = df["transactions"].rolling(30).mean()  # smooth daily fluctuations

print("Monthly totals (last 6 months):")
print(monthly.tail())
print(f"\nTotal 18-month transactions: {df['transactions'].sum():,}")


# STEP 3: Plot for non-technical manager
fig, ax = plt.subplots(figsize=(12, 6))

# Monthly bars
monthly.plot(kind="bar", ax=ax, color="#A8D5BA", alpha=0.7, label="Monthly Total", width=0.8)


# Add 30-day rolling average line on second axis for clarity
ax2 = ax.twinx()
ax2.plot(df.index, rolling_30d, color="#1F4E79", linewidth=2.5, label="30-Day Rolling Average")
ax2.set_ylabel("Daily Average (30-day rolling)", fontsize=12)

# Manager-friendly Titles
ax.set_title("Nairobi Supermarket - Customer Foot Traffic: May 2023 to Oct 2024", fontsize=14, weight="bold", pad=20)
ax.set_xlabel("Month", fontsize=12)
ax.set_ylabel("Total Transactions per Month", fontsize=11)
ax.set_xticklabels([d.strftime("%b %Y") for d in monthly.index], rotation=45, ha="right")

ax.grid(axis="y", alpha=0.3)
ax.legend(loc="upper left")
ax2.legend(loc="upper right")

plt.tight_layout()
plt.savefig("foot_traffic_trend.png", dpi=150)
print("\nChart saved: foot_traffic_trend.png")
plt.show()