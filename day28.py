'''
f-string is also called literal string interpolation
-> literal string: the "f" (string formatting) comes before the main string
-> interpolation: within the string we can embed the variable, function calls or arithmetic operation, etc.
'''

# before python 3.6 we used to do like this
print("Using .format() function\n")
line="Hello, my name is {} and I am from {}"
print(line.format("Rupail", "India"))

# it is hetic if we have changed the sequence
line="Hello, my name is {1} and I am from {0}"
print(line.format("India", "Rupali")) # if we did like this then we need to define the position like 0 or 1 in the line string itself

# we can also round of variable 
price=49.099
print("The price of shoe is ${:.2f}".format(price))
# this is error prone so the better option is using f string

print("Using the f-string: -\n\n")
msg=f"The price of this belt is ${price:.2f}"
print(msg)

# this is very easily understand the string
name="Rupali"
country="India"
welcome=f"Hello, my name is {name} and i am from {country}"
print(welcome)

# sometime we need to really print the {name} on the screen rather the value of name, we can do this like this
mix=f"Using f-string i will can replace the value of {{name }} to be {name }."
print(mix)
# here the {{name }} is literally treated like string and the space after name id printed on screen the ouput is {name }
