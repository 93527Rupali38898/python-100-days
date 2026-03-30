'''Recursion: it is process of defining anything in term of itself'''
# 2 famous example of recusion: Factorial and Fibonacci
def factorial(n):
    '''this function take a value n and return the factorial of this'''
    if (n<0):
        return 0
    if (n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
# let us print the factorial of 7
n1=int(input("Enter the value of n1 (between 1 to 1000): "))
print(f"The factorial of {n1} is {factorial(n1)}")


# let us print the factorial of 1500
n2=int(input("Enter the value of n1 (between 1000 to 2000): "))
print(f"The factorial of {n2} is {factorial(n2)}")
# FIXME: RecursionError: maximum recursion depth exceeded, this is the error i am getting

# by default the limit of recursion if 1000 and we print it using
import sys
print("The default limit of Recursion is:", sys.getrecursionlimit())
# if we want to change the limit of recursion we can do it like this
sys.setrecursionlimit(2000)
# now printint the limit of recursion
print("The changed limit of recursion is:", sys.getrecursionlimit())


n2=int(input("Enter the value of n1 (between 1000 to 2000): "))
print(f"The factorial of {n2} is {factorial(n2)}")



# fibonacci series
def fibonacci(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input("Enter the value of n for fibonacci series: "))
print(f"The {n}th element of fibonacci is {fibonacci(n)}")