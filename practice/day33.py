# we can access the element of python dictionary very fast by key
dic={
    "Rupali":"Goyal",
    "Lalita":"Singh",
    "Riddhi":"Khandelwal",
    "Versha":"Parewa",
    "Rupali":"abc"
    
}
print(dic)
print(dic["Rupali"])   #this will give me output to be abc as python store unique pair of key and if we repeat the key it overwrite it
# print(dic["rupali"])   # FIXME: this will KeyError as rupali is not present in my dic

# here the dic.["rupali"], throw an error but if we want that our program does not throw error even if key does not exists then we use .get("rupali") way to do so
print(dic.get("rupali"))  #this will give output to be None (no Error)


# to access all the key of the dictionary
print(dic.keys())
for key in dic.keys():
    print(f"{key}:{dic[key]}")
    

# to access the value of dictionary
print(dic.values())

# to access the key-value pair in dictionary
print(dic.items())
for key, value in dic.items():
    print(f"{key}:{value}")