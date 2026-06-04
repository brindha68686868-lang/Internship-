# Parent Class
class Animal:
    def sound(self):
        print("Animal makes a sound")

# Child Class 1
class Dog(Animal):
    def sound(self):
        print("Dog barks")

# Child Class 2
class Cat(Animal):
    def sound(self):
        print("Cat meows")

# Polymorphism
animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()