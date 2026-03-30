#                           List and List Comprehensive
# List are ordered, mutuable and dynamic collection that can hold a mix of data items
# 1. Ordered- It means that sequence of data item within the list is preserved
# 2. Mutuable- It means that existing list can be changed
# It means that we can modify the data items of list
# 3. Dynamic-Size of list can be Increased or Decreased 
# as the data item is added or removed from the list
# 4. Hetrogenous- It means that list can store data item of different types, 
# Eg:tuple, dict, integer, string, float, list, etc.

marks=[40, 70, 45, 56, 90, 67, 56]
mixed_list=["Rupali", 19, "Chess", "AI"]
empty_list=[]
print(marks, "has a type:", type(marks), end="\n\n")
print(mixed_list, "has a type:", type(mixed_list), end="\n\n")
print(empty_list, "has a type:", type(empty_list), end="\n\n")



#                           List Index
# Each element in a list has it's unique index
# Index are used to access any particular item in a List 
# In python index counting start from 0
colors=["Red", "Green", "Blue", "Violet", "Black", "Pink"]
#         0       1        2        3        4        5
# len of the list is 6, maximum index possible is "size-1"
print("Value at Index 0 is: ", colors[0])
print("Value at Index 1 is: ", colors[1])
print("Value at Index 2 is: ", colors[2])
print("Value at Index 3 is: ", colors[3])
print("Value at Index 4 is: ", colors[4])
print("Value at Index 5 is: ", colors[5])
# print("Value at Index 6 is: ", colors[6])  #FIXME- We can't Access Element at index 6 
# because maximum possible Index is 5

# Negative Inedxing- Used to access elements from the end of the list.
print("Element at index -1 is:", colors[-1])
print("Element at index -3 is:", colors[-3])
# this are evaluated by python interpreter in this way: -
print(colors[-2])                #output "Black"
print(colors[len(colors)-2])     #output "Black"
print(colors[6-2])               #output "Black"
print(colors[4])                 #output "Black"   
# all has same output


#                                Range of Index
'''You can print a range of list items by specifying where you want to start, 
where do you want to end and if you want to skip elements in between the range.'''

# Syntax : list_name[start:end:jump]
# it will iterate till "end-1" index
print()
animal=["dog","cat", "horse", "pig", "goat", "sheep", "cow", "donkey", "mouse"]
print("Printing - animal[2:-1:2]:", animal[2:-1:2])
# len of animal is 9 so, 
# animal[2:8:2], slicing first then applying jump index
# animal[2:8]=horse, pig, goat, sheep, cow, donkey
#               p      1   p,2    1     p,2     1,      p=print, it is  at index 2
# now applying the jump index of 2, so output will be: ["horse", "goat", "cow"]

# NOTE: If Index are missing and colon is given then, it is assumed as:
# start=0, end=len(list_name), jump=1
# Given that Semicolon is present 
# list_name[:] or list_name[::]
print()
print("Animal[::] :", animal[::])   #output: print entire list
print("Animal[:] :", animal[:])     #output: print entire list


print("\nTrying something new so far:-\n")
print("Len of animal is 9.")
print("animal[-100:-1]", animal[-100:-1])#if start index is negative 
# (even after processing), then also it will start printing from index zero, 
# without a error
# OUTPUT:["dog", "cat", "horse", "pig", "goat", "sheep", "cow", "donkey"]
print("animal[5:3]", animal[5:3])  #print a Empty List

#                    Check whether an item present in list or not
fruit=['banana', 'apple', 'orange', 'pineapple', 'strawberry']
if 'apple' in fruit:
    if 'ple' in 'apple':   # we can even check in string
        print("Apple is present")
else:
    print("Apple is not present")

#                       List Comprehensive
"""List comprehensions are used for creating new lists from other iterables 
like lists, tuples, dictionaries, sets, and even in arrays and strings."""

# List = [Expression for item in iterable if Condition]

# expression: The operation or transformation to perform on each item.

# for item in iterable: Iterates over each item in the iterable (list, range, etc.).

# if condition: (Optional) Filters the items; 
# only items that satisfy the condition are included.

# 1. Basic List Creation: -
new_list=[x**2 for x in range(11)]
print(new_list)

'''new_list2=(x**2 for x in range(11))
print(new_list2)
it made a type<generator>, which return value one by one, if you want to print the data
item use loop or convert it to list, this is usefull when we are dealing with large 
data sets'''

# 2. Adding a condition:
con=[x for x in range(11) if x%2==0]
print(con)

# 3. Nested Loop: 
pair=[(x, y)for x in range(2) for y in range(3)]  #row- 2 and column-3
print("Pair: ", pair)

# 4. List Filteration
lst=[2, 9, 11, 12, 0, -12]
new_lst=[x for x in lst if x >10]
print("lst: ", lst)
print("new_lst with condition x is >10:", new_lst)

# 5. transforming the value of a list
st_lst=["Hello", "You", "sHould", "okay"]
new_strlst=[word.title() for word in st_lst]
print("St_lst:", st_lst)
print("new_strlst:", new_strlst)


# 6. Flattened nested list
nested=[[1, 2, 3], [4, 5], [6], '55']
flat=[y for x in nested for y in x]
print("Nested:", nested)
print("flat:", flat)

# 7. Dictionary key-value pair
info = {"name": "Alice", "age": 30, "profession": "Engineer"}
key_value_pairs = [f"{key}: {value}" for key, value in info.items()]
print(key_value_pairs)
# Output: ['name: Alice', 'age: 30', 'profession: Engineer']



#               Other Important Example of List Comprehensive
# 1. take the world which has letter 'a'
food=['burger', 'pizza', 'apple', 'banana']
a_letter=[x for x in food if 'a' in x]
print("Food:", food)
print("a_letter:", a_letter)

# 2. take the word which has more than 4 characters
name=['ram', 'hari', 'rupali', 'lalita', 'shyam', 'sita']
correct_name=[word.title() for word in name]
print("name: ", name)
print("Correct_name: ", correct_name)
# now finding the name with more than 4 character
more_4_char=[word for word in correct_name if len(word)>4]
print("Name with more than 4 character are:", more_4_char)

