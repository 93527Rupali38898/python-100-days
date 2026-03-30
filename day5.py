#             Comments, Escape Sequence Character and print statement

#comment
# single line comment
print("Hello world")
'''
this is single quote, 
multi line comment
'''

"""
this is double quote, 
multiline comment
"""

# Escape Sequence Character
print("This is good\nbut i doubt sometime")
print("This is \"great\"work by goverment")
print("Other escape sequence character are \\\', \\\", new line-\\n,space-\\t");

# print statement
# print("Hello world", 45, 576, sep=' ', end='\n', file=sys.stdout) 
# error encouter because to use sys.stdout we need to import sys library
# i have written by default values, above, let's change the value and see the result

print("Hello", 56, 78, sep="#", end="&&")
with open('day5.txt', 'w') as f:
    print("Hello", 56, 78, sep="#", end="&&", file=f)