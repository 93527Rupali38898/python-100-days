# Decorator in python
# decorator in python is used when we want to add some extra functionality to the existing function without modifying it


# Example of decorator
def decorator_function(func):
    def wrapper_function():
        print("Wrapper function started")
        func()
        print("Wrapper function ended")
    return wrapper_function

@decorator_function
def show():
    print("Show function")

show()

# questions
# given this lines code write a decorator function that will print the function name before and after the function is called
def decorator(fx):
    def wrapper(*args, **kwargs):
        print("Function Started")
        fx(*args, **kwargs)
        print("Function Ended")
    return wrapper
@decorator
def add(a, b):
    print(a + b)
@decorator
def greet(name):
    print("Hello", name)

add(3, 4)
greet("Rupali")


# decorator to print the total number of arguments passed to the function
def decorArgument(fx):
    def wrapper(*args, **kwargs):
        print("Total Number of Argument:", len(args)+len(kwargs))
        fx(*args, **kwargs)
    return wrapper
        
        
@decorArgument
def login(user, role):
    
    print(user, role)

login("Rupali", role="Admin")
print(login.__name__)



# print the name of the function being run 
from functools import wraps    # to preserve the actual value
def decFunName(fx):
    @wraps(fx)   # this preserve the original name
    def wrapper(*args, **kwargs):
        # print("The name of function is:", fx)  #fx direct print karene se output me function ka address aata hai
        print("The name of function is:", fx.__name__)          
        fx(*args, **kwargs)
    return wrapper
@decFunName
def square(x):
    return x * x
@decFunName
def profile(name, city="Jaipur"):
    print(name, city)
square(3)
profile("Rupali")


print(square.__name__)  #decortor apply hone ke baad function ka name change ho jata hai, to avoid this we use @wraps