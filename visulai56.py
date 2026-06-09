import matplotlib.pyplot as plt

# Sample data
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [120, 150, 180, 170, 210]

# Create line chart
plt.plot(months, sales, marker='o')

# Labels and title
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

# Show chart
plt.grid(True)
plt.show()