import pandas as pd
import matplotlib.pyplot as plt

# Use full path (recommended) or raw string
df = pd.read_csv(r"D:\DEBDEEP SARKAR\HERITAGE ENGINEERING\6th Semester\Internships and Placements\crypto_data.csv")

# Convert Date column to proper datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Filter Bitcoin data
bitcoin = df[df["Crypto"] == "Bitcoin"]

# Sort by date (important for proper plotting)
bitcoin = bitcoin.sort_values("Date")

# Plot
plt.figure(figsize=(10, 5))
plt.plot(bitcoin["Date"], bitcoin["Price"], marker='o')

plt.title("Bitcoin Price Trend")
plt.xlabel("Date")
plt.ylabel("Price")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

