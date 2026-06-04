# Parent Class
class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)

# Child Class
class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no

    def show(self):
        print("Roll No:", self.roll_no)

# Create object
s = Student("Brindha", 101)

# Access parent and child methods
s.display()
s.show()