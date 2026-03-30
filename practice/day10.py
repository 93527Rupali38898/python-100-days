#                               Taking the user input
# by defualt the input we take is always a string datatype but we convert them easily
# using typecasting
a=input("Enter the number 1: ")  # say 12
b=input("Enter the Number 2: ")  #say 23
print("a+b=", a+b)  # output is 1223
# this happened because by default the values are taken as string 
# to resolve this we can do the following
a=int(input("Enter the number 1: "))  # say 12
b=int(input("Enter the Number 2: "))  #say 23
print("a+b=", a+b)  # output is 35
# We can easily typecast into other datatype

# NOTE: we can also write something within the bracket 
# and that will directly print on console
# to highlight within the comment also
# NOTE: imp mark
# TODO: task
# FIXME: things to fix