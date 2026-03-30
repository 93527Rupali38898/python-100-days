'''doc-string and pep8'''
'''
doc-string: this are the string lines written just below the function, method or class. 
This is different from the comment as we can't print the comment at any case, but we can print the doc string 
'''
def square(x):
    '''this function expect a integer value and it return the square of it'''
    return x**2
print(square(5))
print("If we want to print the doc-string: -\n")
print("We use the following syntax: -square.__doc__\n", square.__doc__)

# if we have not written the doc string
def add(x, y):
    return x+y
print(add(4, 5))
print("Doc-string for add function: ", add.__doc__)

# NOTE: If we have written a line and then written doc-string, then it will be treated like normal comment. Eg:
def sub(x, y):
    print(x, y)
    '''this function take 2 number print then and then return it's subtraction'''
    return x-y

print(sub(6, 2))
print("Doc string for sub function: ", sub.__doc__)

# pep8: Python Enhancement Proposal and this was given by Guido van Rossum, Barry warsan and Nick Coghlan in 2001.
'''
PEP8  is to improve the readability and consistency of python code.
A PEP is a document that descibes new feature proposed by python and documet aspect of python like design and style.
'''

'''Zen of Python: if we write import this in shell a poem is printed'''