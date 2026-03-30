# raising custom error
age=int(input("Enter the age: "))
if age<=0:
    raise ValueError("Age can't be negative or zero")
print("The age of User is: {}".format(age))

# we can also do the same using assert but this is mainly used for debugging:
# assert condition, "msg", it raise AssertError if the condition is false, not used in production as assert can be diasabled
assert age<76, "Age can't be greater than 76"


# we can also create a custom error using Oops
