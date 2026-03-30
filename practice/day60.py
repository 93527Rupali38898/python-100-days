# getter and setter in python
class Student:
    def __init__(self, marks):
        if 0<=marks<=100:
            self.__marks = marks  # Private attribute
        else:
            raise ValueError("Marks should be between 0 and 100")
    @property
    def marks(self):
        return self.__marks
    @marks.setter
    def marks(self, value):
        if 0<=value<=100:
            self.__marks=value
        else:
            raise ValueError("Marks should be between 0 and 100")
ram=Student(98)
print(ram.marks)
# ram.marks=990  #FIXME: this raised the ValueError as we are passing number greater then 100 and this is the use of setter
# here we were able to access and modify the private attribute using getter and setter, without it is is not possible at all.


# it is like
# Protected = “please don’t touch”  created like (._)
# Private = “you cannot touch” created like (.__)
# Getter–Setter = only legal access  (@property, @funName.setter)
