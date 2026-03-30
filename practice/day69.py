#  class method
class Employee:
    companyName = "Google"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def changeCompany(cls, newCompany):
        cls.companyName = newCompany

e1 = Employee("Rupali", 4000)
print(e1.companyName)
e1.changeCompany("Apple")
print(e1.companyName)
print(Employee.companyName)