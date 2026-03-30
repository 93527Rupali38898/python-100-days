# Enumerate
lst=['red', 'green', 'blue', 'orange', 'yellow', 'purple']
lst=[word.capitalize() for word in lst]
# if we want index for some reason then
index=0
for element in lst:
    print(f"{index}. {element}")
    index+=1
    
# using enumerate: -
print('\n\nEnumerate: -')
for index, element in enumerate(lst):
    
    print(f"{index}. {element}")
    if (index==0):
        print(type(index), type(element))
    # index+=3  # index here is of no use

# if we don't unpack the things then it will behave like tuple, in the above case we are unpacking it
# without unpacking it
for value in enumerate(lst):
    print(value)
    if (value[0]==0):
        print(type(value), type(value[0]), type(value[1]))
    
# we can also specify the starting index
for index, element in enumerate(lst, start=1):
    print(f"{index}. {element}")