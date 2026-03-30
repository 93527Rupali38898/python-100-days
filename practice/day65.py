# static method in python
class Math:
    @staticmethod
    def add(a,b):
        return a+b

    @staticmethod
    def sub(a,b):
        return a-b

print(Math.add(10,20))
print(Math.sub(10,20))

# this was to show that even we don't need to initalize variable then also we need to pass self in the method, as it will raise an error.

# to avoid this we can initalize such methods using @staticmethod, which means that we don't need to pass self in the method

class Person:
    def __init__(self):
        print("Hello World")
q=Person()