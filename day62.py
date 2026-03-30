# access modifier in python
# there are 3 types of access modifier in python
# 1. public
# 2. protected
# 3. private

# public access modifier
# public access modifier is used to access the variable or method from anywhere in the program
# by default all the variables and methods are public in python

# protected access modifier
# protected access modifier is used to access the variable or method from the same class or from the child class
# to make a variable or method protected we have to use single underscore(_) before the variable or method name

# private access modifier
# private access modifier is used to access the variable or method from the same class only
# to make a variable or method private we have to use double underscore(__) before the variable or method name

# public access modifier example
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def show(self):
        print("Name:", self.name, "Salary:", self.salary)
e = Employee("John", 10000)
e.show()
print(e.name)  # public access modifier
print(e.salary)  # public access modifier

# protected access modifier example
class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
    def show(self):
        print("Name:", self._name, "Salary:", self._salary)
e = Employee("John", 10000)
e.show()
# NOTE: this are not recommended but can be done
print(e._name)  # protected access modifier  
print(e._salary)  # protected access modifier

# private access modifier example
class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
    def show(self):
        print("Name:", self.__name, "Salary:", self.__salary)
e = Employee("John", 10000)
e.show()
# FIXME: this below lines will throw an error 
# print(e.__name)  #this will give error because it is private
# print(e.__salary)  #this will give error because it is private
# we can also do name mangling in python to access private variable or method
print(e._Employee__name)  # this is name mangling
print(e._Employee__salary)  # this is name mangling
# we must use getter and setter method to access private variable or method