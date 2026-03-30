# class, object and self parameter
class Student:
    name="Rupali"
    rollNo=68
    age=20
    def intro(self):
        print(f"The name of student is {self.name} and the roll Number of student is {self.rollNo} and the age of student is {self.age}")
s1=Student()
s1.intro()


class Car:
    
    color="blue"
    model="new"
    mileage=20
    purchases=2025
    def start():
        print("Car Started")
    def info(self):
        print(f"Color:{self.color}\nmodel:{self.model}\nmileage:{self.mileage}\npurchases:{self.purchases}")
maruti=Car()
maruti.start()
maruti.info()

class Laptop:
    def show():
        print("This is a Laptop")
hp=Laptop()
hp.show()
