#                   if else statements
# 1. if statement
# 2. if-else statement
# 3. if-else-elif statement
# 4. nested if-else statement

# NOTE- Relational Operator - <, >, <=, >=, == and !=
# Giving the Examples of all 4 types of conditional statement

# 1. if statement
age=int(input("Enter You Age: "))
if (age>18):
    print("You are Adult Now")

#if age is less than 18 nothing print, 
#and if greater than 18 it will execute the print statement

# 2. if-else statement- when we have two options only
age=int(input("Enter You Age: "))
if (age>18):
    print("You can Vote")
else:
    print("You can't vote")

# if-else-elif statement- when you want to check for multiple condition
num=int(input("Enter the Value of num: ")) 
# here, i am using "int" before every statement to take from input from user 
# is due to the following reason that every user input is by default a string 
# and we typecast that to integer or other datatype

if (num==0):
    print("Num is Zero")
elif (num>0):
    print("Num is Positive")
else:
    print("Num is Negative")

# nested if else statement- it is used when we have some condition under some condition
n=int(input("Enter the value of n: "))
if (n>0):
    if (n<=500):
        print("Number is between 0 and 500")
    elif (n>500 and n<=1000):
        print("Number is between 500 and 1000")
    else:
        print("Number is greater than 1000")
elif (n<0):
    if (n>=-500):
        print("Number is between 0 to -500")
    elif (n<-500 and n>=-1000):
        print("Number is Between -500 and -1000")
    else:
        print("Number is Less than -1000")
else:
    print("Number is Zero")