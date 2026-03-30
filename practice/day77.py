# operator overloading
class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=Student(m1,m2)
        return s3

    def __gt__(self,other):
        r1=self.m1+self.m2
        r2=other.m1+other.m2
        if r1>r2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1,self.m2)

s1=Student(58,69)
s2=Student(60,65)

s3=s1+s2

if s1>s2:
    print("s1 wins")
else:
    print("s2 wins")

a=9
print(a.__str__())

print(s1.__str__())
print(s2)


# doing the same thing for vector
class Vector:
    # defining the constructor
    def __init__(self, i, j, k):
        self.i=i
        self.j=j
        self.k=k
    # defining the print dunder method
    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"
    # defining add operation
    def __add__(self, x):
        return Vector(self.i+x.i,self.j+x.j,self.k+x.k)
    def __sub__(self, x):
        return Vector(self.i-x.i, self.j-x.j, self.k-x.k)
v1=Vector(1, 2, 4)
print(f"The value of Vector v1 is: {v1}")
v2=Vector(2, 4, 5)
print(f"The value of Vector v1 is: {v1}")
print(f"{v1} + {v2} = {v1+v2}")
print(f"{v1} - {v2} = {v1-v2}")
