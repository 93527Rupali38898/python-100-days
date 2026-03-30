#               Function Argument and Return Statement
# 1. Postional Argument: value are matched in the order they are passed
def greet(name, age):
    print("Hello,", name, "!! You are", age,"years old.")
    
name=input("Enter you name: ")
age=int(input("Enter your age: "))
greet(name.title(), age)

# 2. Default Argument: Specify a default value to Parameter
# def average_three_number(a=3, b, c):  #FIXME: This line show Error
# Reason is that non-default parameter come first then default paramter
    
def average_three_numbers(a, b, c=9):
    return (a+b+c)/3
average1=average_three_numbers(4, 5)
# here it is compulsary to give value of a and b, c is optional
# if value of c is given takes that value, else take default value
print("Average is (Defalut value of c is considered):", average1)
# if the value of c is given
average2=average_three_numbers(1, 2, 3)
print("Average is (with c value given):", average2)

# 3. Keyword Argument: we can provide the argument of type, key=value [Like dict]
# Parameters are specified by name.
def name_hobby(name, hobby):
    print(name, "has a hobby", hobby, "!!")
name1=input("Enter the name: ")
hobby1=input("Enter you Hobby: ")
# name_hobby(name=name1.title(), hobby1) #FIXME: This line Show Error
# Reason is Positional argument cannot appear after keyword arguments

name_hobby(hobby=hobby1, name=name1.title())
hobby2=input("Enter your Hobby: ")
name2=input("Enter your name:")
name_hobby(name2.title(), hobby2)

# 4. Variable-Length Argument: Allow passing any number of Argument
# positional variable lenght argument, [type tuple]
def sum_number(*numbers):
    sum=0
    for i in numbers:
        sum+=i
    return sum
sum1=sum_number(1, 2, 3, 4)
sum2=sum_number(1, 2, 3, 4, 5)
sum3=sum_number()
print("Sum of 1, 2, 3 and 4 is: ", sum1)
print("Sum of 1, 2, 3 ,4 and 5 is: ", sum2)
print("Sum of no arguement is: ", sum3)   # output zero, 
# it means it can also except zero argument

# keyword variable length argument, [type dictionary]
def detail(**person):
    for key, value in person.items():
        print(key, ":", value)
person1={"Name":"Rupali Goyal", "Dream":"ML Engineer", "DOB":"03:08:2005"}
person2={"Name":"Lalita Singh", "Dream":"Cardiologist", "DOB":"11:06:2005"}
# we have to put  ** when passing entire dictionary
detail(**person1)
print()
detail(**person2)

# no need to use double star(**), when direct passing argument to function
detail(Name="Rupali Goyal", BFF="Lalita Singh")   
# we don't use quotes before key when passing direct to function


#Other Important Code
def find_max(number):
    maximum=max(number)
    return maximum
numbers=(1,2, 3, 4, 12, 5, 6 ,78, 45)
maximum=find_max(numbers)
print("Maximum among", numbers, "is:", maximum)
# here , we don't use postional variable argument because we are passing a single entity 
# not variable number of argument, here there might be n number of number but it packed

# 5. Required Argument: Argument that are compulsary to pass, otherwise throw "Error".
def greet_person(name):
    print("Hello", name)
# greet_person()  #FIXME: show error because name is reqired argument
