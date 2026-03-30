# finally: the code written in this, will always be executed so this is used to close file resources or databases or for printing delightful message on the screen.
try:
    lst=[1, 2, 4, 5]
    num=int(input("Enter the Index: "))
    print(lst[num])
except Exception as e:
    print(f"The Error Occured is: {e}")
finally:
    print("Close the database")
print("Close database")

# here the code written after the try...except will run no matter error occur or not, so what is the need for the finally, it's main use-case lies in the function in which we return a value, we know as the function returns a value the function terminates but if we have written the finally it will execute no matter the function has returned the value or not
def indx():
    try:
        lst=[1, 2, 4, 5, 6, 7]
        i=int(input("Enter the Index: "))
        print(lst[i])
        return 1
    except Exception as e:
        print(f"The error that occured here is: {e} {i}")
        return 0
    finally:
        print("The function has return the value then also this is executing")
    print("This will not get executed as the function has returned")
z=indx()
print(f"The value that return from the indx function is: {z}")