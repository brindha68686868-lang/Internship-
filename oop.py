# Class definition
class Student:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Create object
s1 = Student("Brindha", 19)

# Call method
s1.display()