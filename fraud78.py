# Simple Fraud Detection Example

transactions = [500, 1200, 300, 15000, 700, 25000]

FRAUD_LIMIT = 10000

for amount in transactions:
    if amount > FRAUD_LIMIT:
        print(f"⚠️ Suspicious Transaction Detected: ₹{amount}")
    else:
        print(f"✓ Normal Transaction: ₹{amount}")