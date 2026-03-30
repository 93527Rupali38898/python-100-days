# map, filter and reduce function: higher order function 
# this functions help us to apply a function over a sequence of elements
# map: help us to apply a function on each element of the list

# map(function, iterable)
def cube(x):
    return x*x*x
l=[1, 2, 4, 5, 6, 2]
# without map
cubel=[]
for item in l:
    cubel.append(cube(item))
print(cubel)

# with map
cubeMap=map(cube, l)
print()
print(cubeMap, type(cubeMap))

# here the dtype of cubeMap is map, which does not produce any output, it just evaluate it and it is memory efficient to see the result we must use the list dtype 
cubeMap=list(map(cube, l))
print()
print(cubeMap, type(cubeMap))



# Filter: used to filter some element out of many
# filter(predicate(assa function jo element ke liye T/F return kare), iterable)
def even(x):
    return x%2==0
print("\nFilter function\n")
l=[1, 2, 43, 45, 5, 2, 25, 64, 2, 45]
filterl=list(filter(even, l))
print(filterl)


# using lambda
cubenew=list(map(lambda x:x**3, l))
print(l, cubenew)

# for reduce we need to import that from the functools library
from functools import reduce
lst=[1, 2, 4, 5, 6, 7]
reducelst=reduce(lambda x, y:x+y, lst)
print(reducelst)
avelst=reduce(lambda x, y: x+y, lst)/len(lst)
print(avelst)