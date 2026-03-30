#              match-case statement
# match case in python is advance as well as flexible
#match-cases in python is used for pattern matching, type matching and for value matching
# we can also match floating value, dictionary, list and tuples using match-case.


# match case as pattern identifier:
data={"Name": "Rohan", "Age":20}
match data:
    case {"Name": abc, "Age":x}:
        print(f"Name: {abc} and age: {x}")
    case _:
        print("Invalid Pattern")
        
# multiple cased example
num=int(input("Enter the Value of Num: "))
match num:
    case 1|2|3:
        print("Value is 1 or 2 or 3")
    case 10|20|30:
        print("Value is 10 or 20 or 30")
    case _:
        print("Default case")

# type matching
value=12
match value:
    case 12:  #check only for 12
        print("It is a integer")
    case "a":
        print("It is a String")
    case _:
        print("It's a default case")

# structure pattern , typle, list and dictionary
# typle
value=(1, 2)
match value:
    case (1, 2):  # Matches the tuple (1, 2)
        print("It's a tuple with 1 and 2.")
    case (1, _):  # Matches any tuple starting with 1
        print("Tuple starts with 1.")
# list
value=[2, 2, 4]
match value:
    case [1, 2, 3]:  # Exact list match
        print("Matched the list [1, 2, 3].")
    case [1, *_]:  # Matches any list starting with 1
        print("List starts with 1.")
    case [*_, 4]:  #matches any list ends with 4
        print("List end with 4")


# deafult case with condition
x = 10
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")
    # Empty case with if-condition
    case _ if x < 10:
        print("x is < 10")
    # default case(will only be matched if the above cases were not matched)
    # so it is basically just an else:
    case _:
        print(x)
        