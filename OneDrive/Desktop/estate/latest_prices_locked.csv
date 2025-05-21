import pandas as pd
import random
import os

# Create folder 'data' if it doesn't exist
os.makedirs("data", exist_ok=True)

# Define neighborhoods and years
neighborhoods = ["Downtown", "Suburb", "Riverside", "Midtown", "Uptown"]
years = list(range(2018, 2025))
data = []

# Generate 200 rows of synthetic real estate data
for _ in range(200):
    year = random.choice(years)
    neighborhood = random.choice(neighborhoods)
    bedrooms = random.randint(1, 5)
    
    # Base price by neighborhood
    base_price = {
        "Downtown": 300000,
        "Suburb": 200000,
        "Riverside": 250000,
        "Midtown": 280000,
        "Uptown": 270000,
    }[neighborhood]
    
    # Final price = base + bedroom effect + some noise
    price = base_price + (bedrooms * 10000) + random.randint(-15000, 15000)
    
    data.append([price, bedrooms, year, neighborhood])

# Create DataFrame
df = pd.DataFrame(data, columns=["price", "bedrooms", "year", "neighborhood"])

# Save as CSV without index and with header
csv_path = "data/latest_prices.csv"
df.to_csv(csv_path, index=False, header=True)

print(f"✅ '{csv_path}' file generated successfully.")

# Example: Load CSV back to check it
df_loaded = pd.read_csv(csv_path)
print(df_loaded.head())

