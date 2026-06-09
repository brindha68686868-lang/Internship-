import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Sample data
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [120, 150, 180, 170, 210, 250]
}

df = pd.DataFrame(data)

# Set seaborn style
sns.set_theme()

# Create plot
sns.lineplot(data=df, x="Month", y="Sales", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)

plt.show()