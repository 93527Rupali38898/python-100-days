# object introseption: dir(), __dict__ and help()

# dir() - show all attributes and methods of an object
# __dict__ - show all attributes of an object
# help() - show documentation of an object

# dir() example
print(dir("hello"))

# __dict__ example
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1.__dict__)

# help() example
print(help("hello"))