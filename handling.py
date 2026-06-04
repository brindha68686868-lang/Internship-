# Write data to a file
file = open("student.txt", "w")
file.write("Name: Brindha\n")
file.write("Course: Python\n")
file.close()

# Read data from the file
file = open("student.txt", "r")
content = file.read()
print(content)
file.close()