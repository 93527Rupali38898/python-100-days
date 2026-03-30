# local and global variables

# global variable
x=10
print(f"The value of x is {x}")
def myfunc():
    # local variable
    x=20
    print(f"The value of x within the function is {x}")
    
myfunc()
print(f"The value of x outside the function is {x}")


# here the value of x is 10 outside the function and 20 inside the function. This is because the variable x is local to the function and the variable x is global to the program.

# to change the value of a global variable inside a function, we can use the global keyword.
print("\nNow using global keyword\n")
x=10
def newfunc():
    global x
    x=30
    print(f"The value of x within the function is {x}") 
print(f"The value of x outside the function before running it is {x}")
newfunc()
print(f"The value of x outside the function after running it is {x}")