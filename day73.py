# dunder method: double underscore method

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __repr__(self):
        return f"Employee('{self.name}', {self.salary})"

    def __str__(self):
        return f"{self.name} - {self.salary}"

    def __add__(self, other):
        return self.salary + other.salary


emp1 = Employee("John", 50000)
emp2 = Employee("Jane", 60000)

print(emp1)
print(repr(emp1))

print(emp1 + emp2)