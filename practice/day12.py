#            len function and string slicing
# we can find out the length of a string using len() function
import sys
a="mango"
b=len(a)
print("Length of", a, "is", b)
print("Sizeof variable a is:", sys.getsizeof("mango"))

# sting slicing
name="Rupali and Lalita"
# indexing start from first till n-1
print(name[0:6])   #print 0 to 5

# we can also do negative indexing
pie = "ApplePie"
print(pie[:5])      #Slicing from Start
print(pie[5:])      #Slicing till End
print(pie[2:6])     #Slicing in between
print(pie[-8:])     #Slicing using negative index
