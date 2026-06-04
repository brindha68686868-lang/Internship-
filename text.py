# Write text to a file
with open("example.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("This is a file handling example.")

print("Data written successfully.")

# Read text from the file
with open("example.txt", "r") as file:
    content = file.read()

print("\nFile Content:")
print(content)