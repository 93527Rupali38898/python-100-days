#                             string and indexing in string
#string is anything that you enclose with ' or " we can also enclose between ''' and """
# string is a sequence or array of character
# string are used when working with unicode number
# Unicode assigns a unique number, called a code point, 
# to every character, symbol, punctuation mark, emoji, or special character.
# unicode is written in hexadecimal number

# character to unicode, input-character and output-unicode code point
print("Unicode of 'A' is", ord('A'))   # 65

# unicode to character, input-unicode code point and output-character
print("Character Associated with code point 65 is", chr(65))    #A

# it does not matter whether you enclose the string with ' or " output remain same
print('He said, "I want to eat an Apple."')
# here no need to use escape sequence character because using different quoation

# mutliline string
print('''He said, "You are look Amazing"
She Replied, "Thanks"
''', chr(9829))



# indexing-start with zero
# square bracket are used to access the element of string
a="Rupali want to Eat Ice-Cream"
b=len(a)
print(a)
print("Lenght of a is", b)
print("Assessing Separate Characters: ")
c=a[0]
print("Index 0 of a has the character", c)
print("Index 1 of a has the charatcer", a[1])

# If i am interested to print the entire string by one by one character, we can use
# for loop in the following way
print("\nAccesing all Character using for loop:--")
i=0
for character in a:
    print("Character at Index", i, "is", character)
    i=i+1

# what if i use multiline for the purpose
c='''Hello Everyone, How are you
I Hope with God's Bless You Will be Fine and Happy'''
print("\n", c)
print("\nAccesing all Character using for loop:--")
i=0
for character in c:
    print("Character at Index", i, "is", character)  
    i=i+1
