# set are unordered pair of collection which store unique element
s={1, 2, 4, 2, 3, 4}
print(s)


# NOTE: set element should be hashable, if we try to take list as a set element, we will encounter error as list can changed and hashable object can't be
# err={1, 2, [2, 4]}
# print(err)
# FIXME: TypeError: unhashable type: 'list'

# to access the element of set
for element in s:
    print(element)
    
# to create a empty set
s1={}
print("type of {} is",type(s1))  # this will show dict
s2=set()
print("type of .set() is", type(s2))