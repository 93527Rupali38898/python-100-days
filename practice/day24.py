#                       Tuple and its slicing
# tuple are similar to list, the only difference between tuple and list is that 
# list can be changed after creation i.e. list are mutable
# tuple are immutable i.e. tuple can't be changed after creation

# Key Feature of Tuple:
# Immutable, Ordered, heterogeneous and allow duplicates

# Crating tuple: -
tup1=(12, 23, 34)
tup2=12, 23, 34
print("Tup1:", tup1, "it's type is:", type(tup1)) #with parenthesis
print("Tup2:", tup2, "it's type is:", type(tup2)) #  packing
print()
# in python packing means combining multiple values into a list or tuple, same as *args

# single element tuple
single_tup1=(1)  #it will have class int
single_tup2=(1,)  # it will have class tuple
# to make a tuple of single element use comma
print("single_tup1:", single_tup1, "it's type is:", type(single_tup1)) 
print("single_tup2:", single_tup2, "it's type is:", type(single_tup2)) 
print()

# empty tuple can be created using parenthesis
empty_tup=()
print("Empty_tup:", empty_tup, "It's type is:", type(empty_tup))
print()

# user input as tuple
user=input("Enter the commma separated data item of tuple: ") #string
lst=user.split(",")   #convert to list
tup=tuple(lst)   # tuple of data item
print("tup:", tup, "it has a type:", type(tup))
print()


#                           Accessing tuple Element
# NOTE: tuple slicing does not modify the tuple indeed it just, return a new tuple.
color=('green', 'blue', 'red', 'pink', 'violet', 'grey', 'black')
#         0        1      2       3       4         5        6      len of color is 7
color1=color[-3] #7-3=4,    OUTPUT: violet

color2=color[-5:-2]  #7-5=2, 7-2=5, color[2:5], (red, pink, violet)
# grey will come in output as slicing it done till end-1 

color3=color[::-2]   #all element and jump is  -2
# output=(black, violet, red, green)

print("color:", color)
print("color[-3]:", color1)
print("color[-5:-2]:", color2)
print("color[::-2]:", color3)
print()


# use case of tuple:
# 1. immutable
# 2. faster than list for involving constant collection
# 3. it can be used as keys in dictionary (because tuple are hashable unlike list)
'''
this point means that, key of dictionary is immutable,
it means it can't be changed after creation
list are mutable and tuple are immutable so can be used as in creation of key 
'''
dict1={}  # key-value pair
my_lst=[1, 2, 3]
# dict1[my_lst]='Value'   # Here my_lst is key and "Value" is it's value
# FIXME: it will raise TypeError as list are unhashable object and 
# key of dictionary must be hashable

my_dict = {}
my_tuple = (1, 2, 3)

my_dict[my_tuple] = "value"  # This works fine!
print(my_dict)  # Output: {(1, 2, 3): 'value'}
print()

# what is the meaning of being hashable
'''
hash means, a process to generate a unique ID for the key.
Being hashable means an object has a hash value that does not change during its lifetime, 
and it can be used as a dictionary key or in a set.

Hashable Object in Python: -
Numbers (int, float, etc.)
Strings (str)
Tuples (as long as all elements in the tuple are also hashable)
'''


#                           Tuple Operation
# 1. concatenation: -
tup1=(1, 2, 3)
tup2=(4, 5)
tup3=tup1+tup2
print("tup1:", tup1)
print("tup2:", tup2)
print("tup1+tup2:", tup3)
print()

# 2. Repition: -
tup=(10, 20)
print("tup:", tup)
print("tup*3:", tup*3)
fruit=("kiwi", 'banana', 'mango')
print("fruit:", fruit)
print("fruit*2:", fruit*2)
print()

# 3. Membership Testing: - (in keyword)
print("if 'kiwi' in fruit", 'kiwi' in fruit) # return boolean expression
if 'pineapple' in fruit:  # 'pineapple' in fruit will return True or False
    print("Pineapple is present in fruit basket")
else:
    print("My fruit basket does not have Pineapple")

print()

# 4. Lenght of tuple: -
dry_fruit=('almond', 'cashew', 'walnut', 'groundnut')
print("dryfruit:", dry_fruit,"has a length of:", len(dry_fruit))
print()

# 5. Iteration through a tuple: -
print("fruit:", fruit)
for i in fruit:
    print(i)
    # we can also iterate through each string under the tuple
    for char in i:
        print(char)
    print()
        
        
        
