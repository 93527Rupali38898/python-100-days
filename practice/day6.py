#                         Variable and Datatype
# Variable: It is like creating a placeholder and assigning it some value 
# variable hame ye btati hai ke ham kis type ka data store kr rhe hai, 
# and jha store ho rhi hai usse ek particular tag dene me kaam aati hai,like: 
example=1
# as i have written this, 1 get stored in memory and 
# the location in memory where the 1 is stored is given a tag as "example" 


# datatype
# 1. Numerial: int, float, complex
a=123
b=78.65
c=complex(5, 2)
print("The value of a is: ", a)
print("The value of b is: ", b)
print("The value of c is: ", c)
print("Now Printing the Datatype of all three")
print("Datatype of a is: ", type(a))
print("Datatype of b is: ", type(b))
print("Datatype of c is: ", type(c))


# 2. String-Sequence of Character
a="Rupali is Doing this Coding on 10 dec" #overwrite the value of a
print("The value of a is: ", a)
print("Datatype of a is: ", type(a)) 

# 3. Boolean- True or False
p=True
print("The Value of p is: ", p)
print("Datatype of p is: ", type(p))

# 4. NoneType- None- used to define no value or null datatype
r=None
print("The value of r is: ", r)
print("Datatype of r is: ", type(r))

# 5. Sequenced data: List, Tuple- ordered collection of different datatype
# list- Mutuable (can be changed)
# tuple-immutuable(can't be changed) 
abc=[12, 34.5, "Rupali", True, complex(12, 3), (45, None), ["Done"]] #list
pqr=(45, 67.8, [56, 89.9], "apple")  #Tuple
print("The value of abc is: ",abc)
print("The value of pqr is: ",pqr)
# printing the datatype also
print("Datatype of abc is: ", type(abc))
print("Datatype of pqr is: ", type(pqr))


# mapped datatype: Dictionary
y={"Name": "Rupali", "Age": 19, "Interest": "Coding"}
print("The value of y is: ", y)
print("Datatype of a is: ", type(y))