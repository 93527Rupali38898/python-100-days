# multiple inheritance
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Salary:
    def __init__(self, salary):
        self.salary = salary

class EmpDetails(Employee, Salary):
    def __init__(self, name, id, salary):
        Employee.__init__(self, name, id)
        Salary.__init__(self, salary)

    def display(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Salary: {self.salary}")

# Example usage
emp = EmpDetails("John Doe", 12345, 50000)
emp.display()