# Create a class
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)

# Create objects
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "City")

# Access object methods
car1.display()
print()
car2.display()