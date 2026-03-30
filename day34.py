# dictionary method for manuplation
dic1={
    "Riddhi":"Khandelwal",
    "Rupali":"Goyal",
    "Versha":"Parewa",
    "Lalita":"Singh"
}
dic2={
    "Vishal":"Kumar",
    "Saroj":"Bala",
    "Neeru":"Garg"
}
print(dic1)
print(dic2)
dic1.update(dic2)
print("Updated dic1 after updation: ", dic1)

# clear function
dic2.clear()
print(dic2)

# pop(): remove key-value pair, if key not in dic the raise KeyError
print(dic1.pop("Rupali"))
print("After poping Rupali:", dic1)
# print(dic1.pop())  #FIXME: It raises TypeError
# if we don't mention anything then raise TypeError

# popitem(): it remove the last item and does not take any parameter
print(dic1.popitem())
print("After poping last key value pair:", dic1)

# del keyword: it is not a function 
dic3={
    "Rupali":"Person",
    "Spoon":"Object",
    "Tommy":"Dog"
}
print(dic3)
del dic3
# print("After deleting the dictionary: ",dic3)  #it raise an error NameError

# we can also delete the a particular key also 
del dic1["Riddhi"]
print("After deleting Riddhi:", dic1)
# if key not in dict then throw KeyError

