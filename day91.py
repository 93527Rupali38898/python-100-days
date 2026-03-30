# generator in python
def gen_func(n):
    for i in range(n):
        yield i*i

# creating an generator function
gen=gen_func(100)
print(f"The generator object is {gen}")   #this print the generator object
print(f"The 1 element is {next(gen)}")   #first element
print(f"The 2 element is {next(gen)}")   #second element
print(f"The 3 element is {next(gen)}")   #third element

# we can also iterate over the generator function using for loop
for i in gen:
    print(i)
