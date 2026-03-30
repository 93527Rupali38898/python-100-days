# we use this if we don't know how many function do we need to import and we decide it as we are writing code 
import math as m
pie=m.pi
print(pie)

# in the below notation, there is no need to write the name of library as we are already importing specific function from module so no need to write module name, we use this when we have less number of function and we know in advance what function we are going to use

from time import time
sec=time()  #here no need to write time.time
print(f"Time since epoch is {sec}")

# importing using wildcart
from random import *
lst=[12, 23, 4,5]
num=choice(lst)
print(num)

# here also there is not need to write the name of module, but it is not recommened in python because if two function name are same in two module then we can see unexpected behavior

# to know more about modules 
print(dir(m))  # to know the names of the function in the module
# print(help(m))  # to know more infomation about each function and description about the module

# import the function written by us
import greeting
# function in the greeting

greeting.welcome("Rupali")
greeting.sum()
print(greeting.fact)   # a variable defined in the greeting