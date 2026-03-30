# set operation
# union and update
cities1={'tokyo', 'berlin', 'madrid', 'delhi'}
cities2={'tokyo', 'seoul', 'kabul', 'madrid'}
# if we want that our original sets remain intact, then:
cities3=cities1.union(cities2)
print(cities3)

# update change the original set
# cities1.update(cities2)
# print(cities1)


# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# interaction and interaction_update()
print(cities1.intersection(cities2))

# to change the original set
# cities1.intersection_update(cities2)
# print(cities1)

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# symmetric difference: union of two set - intersection of 2 set
# in short the symmetric difference print the element which are not common in both the set
cities3=cities1.symmetric_difference(cities2)
print(cities3)
# to update the original set
# cities1.symmetric_difference_update(cities2)
# print(cities1)


# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# difference(): it return a new set which contain the element of original set but not in other set, like there are 2 set (A, B): A.difference(B) is equal to A-B

cities3=cities1.difference(cities2)
print(cities3)
# to update the original set
# cities1.difference_update(cities2)
# print(cities1)



'''                     Several In-built function in python'''
# 1. disjoint: the set which have no element in common, if the element is disjoint the function return True, else return False
print("Several Other function: \n\n")
print(cities1.isdisjoint(cities2))


# 2. issuperset: if all other element present in the set1
print(cities1.issuperset(cities2))

# 3. issubset(): just opposite of issuperset method, it check if all the element of original set present in the particular set

print(cities1.issubset(cities2))

# 4. to add a single element in the set
print("Cities 1:", cities1)
cities1.add("Mumbai")
print("After adding an element:", cities1)

# 5. remove: remove the element from the set, if the element not present in set raise ValueError

print("Cities 1:", cities1)
cities1.remove("delhi")
print("After removing an element:", cities1)

# 6. discard: remove the element from the set, if the element not present in set does not raise KeyError

print("Cities 1:", cities1)
cities1.discard("delhi")
print("After discarding the element not in set:", cities1)

# 7. pop: remove an random element from the set and we can even print the popped element

print("Cities 1:", cities1)
element=cities1.pop()
print("After poping the element:", cities1)
print("The popped element is:", element)

# del: it is not a function, it is a keyword which delete the entire set
print("Cities2: ", cities2)
del cities2
# print(cities2) 
# FIXME: as we deleted the cities2, if we try to access it we get NameError

# clear(): this delete are the element of the set, not the set
print("Cities1: ", cities1)
cities1.clear()
print("After clearing the cities1: ", cities1)

print(cities3)

if 'delhi' in cities3:
    print("Yes delhi is present")
else:
    print("Delhi is not Present")
    