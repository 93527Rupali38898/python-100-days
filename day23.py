#                   List method
# take user input list
'''lst=list(input("Enter the list: "))
print("User input list is:", lst)
# problem with this code is that it take each entered element as the data item of list
# Enter the list: 12, harry
# User input list is: ['1', '2', ',', ' ', 'h', 'a', 'r', 'r', 'y']'''

# # better approach is
# str1=input("Enter the data items of list(space separated): ")
# lst1=str1.split()
# print("List is:", lst1)

# str2=input("Enter the data items of list(comma separated): ")
# lst2=str2.split(',')
# print("List is:", lst2)


frt=['apple', 'bananA', 'cherry', 'orange', 'mango', 'kiwi', 'pineapple']
#       0         1         2         3        4       5        6
fruits=[word.capitalize() for word in frt]
print("My Fruit Basket has Fruit name:", fruits)

# Applying method on list, before that finding out it's, lenght of data points
length=len(fruits)
print("Number of fruit in fruit basket is:", length)
print()

# 1. Append()- Adding a new fruit  in my basket  -[1] argument
fruits.append('Pear')
print("After appending Pear:", fruits)
# fruits.append()   #error as function accept exactly 1 argument
print()

# 2. Extend(iterable)- add new iterable in my fruit basket  -[1] argument
temp=(12, "Plum")
fruits.extend(temp)
print("Fruit after extending with", temp, "it becomes:\n", fruits)
print()

# 3. insert(index, item)- insert the item at a particular index-[2] argument
fruits.insert(3, "Coconut")
print("After inserting coconut at index 3: \n", fruits)
print()

# 4. remove()- remove the first occurance of the specified item    -[1] argument
# fruits.remove('lemon')  #FIXME- because lemon not in list, so show error
fruits.remove('Kiwi')   #case sensitive
print("Kiwi removed from the list:\n", fruits)
print()

# 5. pop(index)- remove and return the element whose index is given    [0 or 1] argument
poped1=fruits.pop()
print("Pop function used without providing the index(last element removed):\n", fruits)
print("Fruit removed was:", poped1)
poped2=fruits.pop(4)
print("Pop function and we removed the element at index 4:\n", fruits)
print("Fruit removed was:", poped2)
# poped3=fruits.pop(60) #FIXME- Raise IndexError as it cross the maximum index
print()

# 6. clear()-remove all data items of list  -[0] argument
fruits.clear()
print("Clear function: ", fruits)
print()

# 7. index(item, start, end)- return the first occurance of the item
# item is compulsary argument and start and end are optional - [1,2, 3] argument
color=['Red', 'Green', 'Red', 'Pink', 'Blue', 'Green', 'Violet']
#        0       1       2       3       4       5         6
green_index=color.index('Green')
print("Red is at Index:", green_index)
red_index_specified=color.index('Red', 2, 4)
print("Red in at Index:", red_index_specified, "Between 2 to 4")
# black_index=color.index('Black') #FIXME- Show error because black not in list
# empty_index=color.index()  #error as 1 argument is compulsary
print()

# 8. count(item)-count the number of occurrences of the item -[1] argument
count_red=color.count('Red')
print("Number of times Red in List is:", count_red)
count_green=color.count('Green')
print("Number of times Green in List is:", count_green)
count_black=color.count('Black')
print("Number of times Black in List is:", count_black) # OUTPUT-0
# empty_count=color.count() #Error as it accept exactly 1 argument
print()

# 9. sort(reverse=True, key=none)     -[0, 1, 2] Argument
print("Color:", color)
'''ascending_color=color.sort()
print("Ascending order of color:", ascending_color)
descending_color=color.sort(reverse=True)
print("Descending order of color:", descending_color)'''
#output will be NONE as sort method does not return anything indeed it just sort the list
color.sort()
print("Ascending order of color:", color)
color.sort(reverse=True)
print("Descending order of color:", color)


# key argument is used to tell what criteria we are taking for the sorting
# eg: if integer list, lst=[1, 2, -5, 3, -6]
# lst.sort(key=abs), absolute value ke basic pe sort kare
# output-[1, 2, 3, -5, -6], other example could be key=len, etc

print()

# 10. reverse()- reverse the list in place   - [0] argument
ne=['lalita', 'rupali', 'gursneh', 'versha', 'nerru']
name=[word.capitalize() for word in ne]
print("Names are:", name)
name.reverse()
print("Order of Name are Reverse:", name)
print()

# 11. copy()- make a shallow copy of the list  -[0] argument
print("Name:", name)
print("A new list is made named friend and has value similar to name")
print("Changing friend:--\n")
friend=name
friend[0]='Sita'
print("Name:", name)
print("It got changed evem if we have only changed friend")
print("So:--\n")

# correct way: -
print("Name before Updation:--\n")

friend=name.copy()
friend[0]='Nerru'
print("Name:", name)
print("Friend", friend)
print("Name does not changed this time")
print()


# 12. del (not a method but useful)
# syntax del list_name[index]
vehicle=['car', 'bike', 'aeroplane', 'helicopter', 'ship']
print("Vehicle:", vehicle)
del vehicle[1]
print("Deleted the 1  index:", vehicle)
# del vehicle [45] #FIXME - error as out of index
del vehicle[:]
print("Deleted entire data item of vehicle:", vehicle)   #empty list
# NOTE: This methods are changing my original list, this is possible as list is mutuable




#                   Concatenation of 2 list
color1=['red', 'green', 'violet']
color2=['pink', 'black','brown']
colors=color1+color2
print("Color 1:", color1)
print("Color 2:", color2)
print("Color1 + Color2:", colors)

# NOTE- difference between direct concatenation and extend method is that 
# entend method extent the iterable in the existing list
# but this return a new list
