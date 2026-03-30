#                           Tuple Operations
# Tuples has only 2 in-built functions
# 1. count(item)= Return the count of the item in the tuple
# 2. index(item, start, end)= return the index of the first occurance of the item

# count(item)
color=("red", 'green', 'violet', 'green', 'red')
#        0       1        2         3       4   
count_green=color.count('green')
count_violet=color.count("violet")
count_pink=color.count('pink')
print("Color:", color)
print("Number of times \"green\" occur in color is:", count_green)
print("Number of times \"violet\" occur in color is:", count_violet)
print("Number of times \"pink\" occur in color is:", count_pink)
print()

# index(item, start, end)
index_green=color.index('green')
index_red=color.index("red")
index_red_n=color.index('red', -71, 10)

# index_red_1_4=color.index('red', 1, 4) #FIXME - error because slicing happen till end-1 
# output of color[1:4]=(green, violet, green)
# red not in tuple, so raise ValueError
# item not present in tuple and you asking it's index, that's why raise error
 
index_red_end=color.index('red', 1)  # take the end to be len(tuple)  (by default)
print("Color:", color)
print("Green in my Tuple has index:", index_green)
print("Red in my Tuple has index:", index_red)
print("Red in My tuple has the index [start=-71, end=10]:", index_red_n)
print("Red in my Tuple has index [start=1 and end=len(tuple)]:", index_red_end)


# unpacking  of the tuple
coordinates = (10, 20, 30, 40)
x, y, z, t = coordinates
print(x, y, z, t)  # Output: 10 20 30
# NOTE: number of element in tuple and number of unpacking variable should match 
# overwise it will raise ValueError.



# Tuple are immutable, if they contain mutable object then that object can be modified
tup=(1, [2, 3])
print("tup:", tup)
# tup[0]=23  #FIXME: error as interger is also immutable in itself
tup[1][1]=34
print("Tup update:", tup)
print()

# if i want to change my tuple, then first i have to convert into list, 
# then perfrom changes and then again convert it into tuple
fruit=('banana', 'mango', 'almond', 'strawberry', 'grapes')
print("fruit:", fruit)
# it is tuple now so, we can't modify it
# we have to remove almond as it is not a fruit and 
# want to add insert watermelon at index2
# first convert it into list
lst=list(fruit)
lst.remove('almond')
lst.insert(2, 'watermelon')
# also formatting the list
lst2=[word.capitalize() for word in lst]
fruit=tuple(lst2)
print("Updated fruit:", fruit)