import numpy as np

# Sample data
marks = np.array([78, 85, 90, 67, 88, 92, 75, 81, 95, 70])

# Basic statistics
print("Marks:", marks)
print("Total:", np.sum(marks))
print("Average:", np.mean(marks))
print("Maximum:", np.max(marks))
print("Minimum:", np.min(marks))
print("Median:", np.median(marks))
print("Standard Deviation:", np.std(marks))

# Students scoring above average
above_avg = marks[marks > np.mean(marks)]
print("\nMarks above average:", above_avg)

# Sort data
sorted_marks = np.sort(marks)
print("\nSorted Marks:", sorted_marks)