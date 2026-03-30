#super keyword: used to call the constructor of the parent class
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)   # parent constructor
        self.marks = marks

s = Student("Rupali", 90)
print(s.name)    # Rupali
print(s.marks)   # 90
