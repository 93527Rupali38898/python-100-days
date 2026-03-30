#                        for loop 
# Iteration- to repeat a set of instruction again and again
'''for loop is used to iterate over a sequence of elements 
(tuple, list, string, range and other iterable object)'''

# syntax: - for variable in iterable:

# variable: This takes on the value of each element in the iterable, one at a time.
# iterable: An object that can return elements one at a time, like lists, range, etc
fruits=["apple", "cherry", "banana", "mango"]
for fruit in fruits:   #iterating the element of list
    print(fruit)
    print("[", end=" ")
    for char in fruit:  #for interation the string present in list
        print(char, end=", ")
    print("]")
print()

# Iterating over the Sequence of Number: 

# for loop print till n-1, not print n
for i in range(10, 1):  #print nothing as by default the step count is to 1
    print(i)
print()

# this block of line means that the number start with 10 and goes till 1 
# with incrementing 1 each time, the condition is false so nothing print.

for i in range(10, 1, -1): # 1 will not print, it will not print 1
    print(i)
print()

# for i in range(1, 10, 0): # FIXME- 3rd argument of for loop can't be zero,  
#     print(i)
# if the 3rd argrument of for loop is 0 that means we are not incrementing (ValueError)

# nested for loop is used very widely, eg:- matrix, star pattern
for i in range(3):
    for j in range(2):
        print("i=", i, "and j=", j)
print()
#For each value of i, the inner loop will execute first, and then i will be incremented.

# iterating tuple
colors=("Green", "Blue", "Red")
for color in colors:
    print(color)
print()

# iterating key value pairs of dictionary
information={"Name":"Rohan", "Age": 20, "Profession":"Doctor", "Hobby":"Games"}
for key, value in information.items(): # for accessing key-value pair 
    print(key, ":", value)    
print()
    
for value in information.values(): #for accesing the value of dictionary item
    print(value)
print()

# for accessing the key of the dictionary we have two options:
for key in information:
    print(key)
print()

for key in information.keys():
    print(key)
print()