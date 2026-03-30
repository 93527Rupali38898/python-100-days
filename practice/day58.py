# constructor in oops
# there are two types of constructor
# 1. default constructor
# 2. parameterized constructor

# default constructor

class student:
    def __init__(self):
        print("this is default constructor")

    def show(self,name):
        print("hello",name)

s1=student()
s1.show("sai")

# parameterized constructor

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print("hello",self.name,"your age is",self.age)

s1=student("sai",20)
s1.show()


# question to understand the parameterized constructor
class Person:
    def __init__(self, name):
        self.name=name
    def display(self):
        print(f"Hello, my name is {self.name}")
ram=Person("Ram Sahu")
ram.display()

class Book:
    def __init__(self, title, author):
        self.author=author
        self.title=title
    def show_detail(self):
        print(f"Title:{self.title}\nAuthor:{self.author}")
jungle=Book("Jungle Book","Rudyard Kipling")
jungle.show_detail()