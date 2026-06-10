import pandas as pd

# Sample machine data
data = {
    "Machine": ["M1", "M2", "M3", "M4", "M5"],
    "Temperature": [45, 50, 95, 55, 110],
    "Pressure": [120, 125, 180, 130, 200]
}

df = pd.DataFrame(data)

print("=== Machine Analytics Report ===")
print(df)

# Detect abnormal machines
print("\n=== Alerts ===")

for index, row in df.iterrows():
    if row["Temperature"] > 90:
        print(f"⚠ High Temperature Alert: {row['Machine']}")

    if row["Pressure"] > 170:
        print(f"⚠ High Pressure Alert: {row['Machine']}")