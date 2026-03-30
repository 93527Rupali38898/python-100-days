# lambda functions

# lambda arguments: expression

# def add(a,b):
#     return a+b

minus = lambda x,y: x-y

print(minus(9,4))

def fun(fx, val):
    return fx(val)+7
print(fun(lambda x:x*2, 6))




# question 1
# add two numbers
add= lambda x,y: x+y
print(add(5, 7))

# question 2
check=int(input("Enter the number for odd/even: "))

odd_even=lambda x:"even" if x%2==0 else "odd"
print(odd_even(check))

