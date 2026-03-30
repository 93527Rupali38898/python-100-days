# Exception handling in python
# hanlding all error and printing a msg
try:
    num=int(input("Enter the number: "))
    for i in range(1, 11):
        print(f"{num} X {i} = {num*i}")
except:
    print("Error Encounter")

# printing the error
try:
    num=int(input("Enter the number: "))
    for i in range(1, 11):
        print(f"{num} X {i} = {num*i}")
except Exception as e:
    print("Error Encounter: ", e)
    
# handling a specific error
try:
    num=int(input("Enter the number: "))
    for i in range(1, 11):
        print(f"{num} X {i} = {num*i}")
except TypeError:
    print("TypeError")
except ValueError:
    print("ValueError")
except Exception as e:
    print("Error Encounter: ", e)
    
'''
1. ZeroDivisionError: Attempting to divide a number by zero.
2. NameError: Referring to a variable or function that has not been defined.
3. TypeError: Performing an operation on an incompatible data type (e.g., adding a string to an integer).
4. IndexError: Accessing an index outside the bounds of a list or other sequence.
5. KeyError: Trying to access a non-existent key in a dictionary.
6. ValueError: Jab data type sahi hota hai, lekin uska value galat hota hai, tab ValueError aata hai.
'''