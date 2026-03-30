# multilevel inheritance in python
class Human:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"Name:{self.name} Age:{self.age}"
class Employee(Human):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary=salary
    def __str__(self):
        return f"{super().__str__()} Salary:{self.salary}"
class Programmer(Employee):
    def __init__(self, name, age, salary, lang):
        super().__init__(name, age, salary)
        self.lang=lang
    def __str__(self):
        return f"{super().__str__()} Language:{self.lang}"
p1=Programmer("Rupali", 20, 60000, "Python")
print(p1)