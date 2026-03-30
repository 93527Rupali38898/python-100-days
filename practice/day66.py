# instance and class variables
class Employee:
    company_name = "Google" # class variable

    def __init__(self, name, salary):
        self.name = name # instance variable
        self.salary = salary # instance variable

    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary} and the company name is {self.company_name}")

emp1 = Employee("Harry", 100000)
emp1.show()

emp2 = Employee("Rohan", 200000)
emp2.show()

emp1.company_name = "Apple" # instance variable
emp1.show()
emp2.show()
Employee.show(emp1)  # this is same as emp1.show()