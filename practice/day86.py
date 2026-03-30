# walrus operator (:=) in python

# The walrus operator is a new feature in Python 3.8 that allows you to assign values to variables as part of an expression.
num=[1, 2, 3, 4, 5]
while(n:=len(num)) > 0:
    print(num.pop())
    
    
    
# creating a menu driven program using walrus operator
# color=list()
while(color:=input("Enter a color: "))!="quit":
    print(color)