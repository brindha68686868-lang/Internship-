import pandas as pd

# Sample data
data = {
    "Name": ["Arun", "Priya", "Kumar", "Divya", "Rahul"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 92, 78, 88, 95]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display data
print("Student Data:")
print(df)

# Basic analysis
print("\nAverage Marks:", df["Marks"].mean())
print("Maximum Marks:", df["Marks"].max())
print("Minimum Marks:", df["Marks"].min())

# Students scoring above 85
print("\nStudents scoring above 85:")
print(df[df["Marks"] > 85])

# Sort by marks
print("\nSorted by Marks:")
print(df.sort_values(by="Marks", ascending=False))

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())