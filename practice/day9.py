#                               Typecasting
# it simply refer to change the datatype of a variable to other datatype
# python provide different kind of in build function for typecasting
# two type of typecasting: implicit and explicit
# implicit: convert by python interpereter automately

a=12
b=34.4
print(a+b)  # give float answer


# explicit: we convert by our wish
'''
1. type converison function-int, float, string
'''
# int
a="12"
b=int(12)
print("The datatype of b is: ", type(b))

# float
b=12.4
a=int(b)
print("The datatype of a is: ", type(a))

# string
abc="123.4"
# i=int(abc)  #encounter error as string is in float datatype
f=float(abc)
print("The datatype of abc is: ", type(abc))
# print("The datatype of i is: ", type(i))
print("The datatype of f is: ", type(f))
print("Converting abc to float and printing it's datatype", type(float(abc)))


'''
2. Character and Number Conversion: ord(), hex(), oct()
'''
# ord()- convert into it's unicode (ASCII)value
a='A'
b=ord(a)
print(b)
print("Datatype of b is : ", type(b))

# hex()- convert number into it's hexadecimal number
a=255
b=hex(a)
print(b)
print("Datatype of b is : ", type(b))  #return datatype to be str(hexadecimal tha)

# oct()- convert number into it's octal number
a=255
b=oct(a)
print(b)
print("Datatype of b is : ", type(b))  #return datatype to be str(octal tha)

'''
3. Data Structure Creation : tuple(), set(), list(), dict()
'''
a=tuple([1, 2, 3])
print("Tuple", a)
b=set([1, 2, 2, 3])
print("Set", b)
c=list("abc")
print("List", c)
d=dict([(1, 'a'), (2, 'b')])
print("Dictionary", d)
