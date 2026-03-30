# class method as alternate constructor
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):
        name, age = string.split(',')
        return cls(name, age)

person = Person.from_string("John, 25")
print(person.name, person.age)