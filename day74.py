# method overloading in python

class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")

d = Dog()
d.sound()


# Output: Dog barks