#                        string method (23)
# upper(), lower(), strip(), rstrip(), replace(), split(), capitalize()
# center(), count(), endswith(), startswith(), find(), index(), isalnum(), isdigit()
# isalpha(), islower(), isupper(), isprintable(), isspace(), istitle(), swapcase(), title()

''' 
methods that does not take any argument: 13
upper(), lower(), capitalize(), isalnum(), isdigit(), isalpha()
islower(), isupper(), isprintable(), isspace(), istitle(), swapcase(), title()
'''


'''
strings are immutable, 
means strings can't be changed but we can perform method on string

This methods does not change the string but apply method on a copy of string
'''

# 1. upper()-convert the string in upper case
up="A Lion Live in JunGle"
print("Normal String: ", up)
print("Applying Upper function on String, now is: ", up.upper())
# print("Applying Upper function on String, now is: ", up.upper(4)) #show error
print("After Applied Upper() (original up): ", up)  #does not change by upper method

# 2. lower()-convert the string in lower case
print("Lower Function on string: ", up.lower())

# NOTE: upper() and lower() take no argument


# 3. strip-remove white space before and after the string
st="    You     can see Original one   "
print("st:", st)
print("st.strip:", st.strip())  #does not remove extra space betwen you and can
# if no argument in strip function directly remove the leading and trailing white spaces
# if argument is given then, if the given sequence of character are leading or trailing 
# character removes that
st="You can see Original one"
print("st:", st)
print('st.strip("You"):', st.strip("You"))  #remove you (starting)
print('st.strip("Y"):', st.strip("Y"))  #remove y (starting)
print('st.strip("one"):', st.strip("one"))  #remove one (trailing)


# 4. rstip()-remove the trailing character
rst="       !!!!!!!Hello!!!!!!!!       "
print("rst:", rst)
print("rst.rstip():", rst.rstrip())  
#no argument then remove whitespace and \n from the end of string
print("rst.rstrip(\"!\")", rst.rstrip("!")) #give same output, let's remove " " from end
rst="   !!!!!!!!!Hello!!!!!!"
print("rst.rstrip(\"!\")", rst.rstrip("!")) #remove the trailing '!' this


# 5. replace()-replace all occurance of a string to other string
rep='''
twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.
twinkle, twinkle, little star,
'''
print("rep:", rep)
print("twinkle->ringle: ", rep.replace("twinkle", "ringle")) #change all occurance
# NOTE: replace("old", "new", count) method in python can take 2 or 3 argument
# no 2 argument given change "all" occurance,
# if count metioned change that number of times
print("twinkle->ringle: ", rep.replace("twinkle", "ringle", 3)) #change 3 occurance

# 6. split()-split string into different items of list
name="Rupali, Versha, Lalita, Gursneh"
print("Name:", name)
print("Name List:", name.split(",", 3))  #index start from 0 print all
print("Name List:", name.split(",", 2))  #index start from 0 as r, 1 as v and 2 as l,g
'''NOTE: split("separator", max count)
both the argument is optional
if 1 omitted, separate via space, tab or new line
if 2 omitted, convert all string word in list else convert till the number+1
'''

# 7. capitalize()-convert the first letter capital and rest all in lower case
cap="you SHOUld Not dO it."
print("cap:", cap)
print("cap.capitalize():", cap.capitalize())
# take no argument

# 8.center()-align the string to the center
cen="I am going to align the string in center"
print(cen)
print(len(cen))
print(cen.center(80))  #missing the second paramter will result in addition of spaces
print(len(cen.center(80)))  #len become 40 to 80
# in center() it is compuslary to give 1 argument that is integter and other is optional
print(cen.center(80, "."))
print(cen.center(30, "."))  #no effect
print(cen.center(41, "."))  # one dot before the string
# this function align to the center if the parameter in function is greater than len(str)

# 9. count()- return the number of times a given item occured in the string
cou="A item, a book, a a table, the sun, the moon, the earth, the universe"
print("Count of the:", cou.count("the"))
otherex="ananananaaaaaaaaaaaa"
slic=otherex[1:10] #output-nanananaa (till n-1, 10-1=9 tk he liya)
print(slic)
print("count a from 1 to 10: ", otherex.count('a', 1,  10)) #till n-1
# in count() method, 1 argument is compulary, and start and end index is optional
# count('element', start_index, end_index)

# 10. endswith()-whether a given string end with a specified suffix 
# string.endswith(suffix, start, end), suffix is required and 
# start and end index is optional
data='data.csv'
# print("Endswith csv or py: ", data.endswith('.csv', '.py')) #FIXME: wrong way to write
# i have make tuple of the suffix
print("does the data endswith .csv or .py: ", data.endswith(('.csv', ".py")))

text = "The quick brown fox"  # by 10 to 15 we sliced brown from the string
print(text.endswith("brown", 10, 15))  # Output: True, n-1 till end index


# 11. startswith()- very similar to endswith(), but checks prefix
# startswith(prefix or tuple of prefix, start, end)
st="hello World"
print(st)
print("Start with hello? ", st.startswith("hello"))
eg='you are welcome'
print(eg)
print("startwith (your or mine)? ", eg.startswith(("your", "mine")))


# 12. find()-find the first index of the element, if the value is absent return -1
# find(element, start, end)
fn="you are mine, i will always protect you."
print("st:", fn)
print('fn.find("mine")', fn.find("mine")) #output 8
print('fn.find("Love")', fn.find("Love")) #output -1 (because in string)


# 13. index()-similar to find but it gives error if element not found in string
# index(element, start, end)
print('fn.index("mine")', fn.index("mine")) #output 8
# print('fn.index("Love")', fn.index("Love")) #output -raises ValueError


# 14. isalnum()-if the entire string only contain, a-z, A-Z, or 0-9 
# if empty string return false
username=input("Enter the User name: ")
if username.isalpha():
    print("Valid username")
else :
    print("Invalid username, only charcter and digit are allowed")
    
# 15.isdigit()- only digit are present (useful for OTPs)
otp=input("Enter the Otp: ")
if otp.isdigit():
    print("Valid value for otp")
else:
    print("Invalid value for OTP")
    
# 16. isaplha()- very similar to isdigit(), it only aphabetical character
abc="abcdsAHJDHJ"
print(abc)
print("abc.lower()", abc.isalpha())  #return true
abc="abcdsajhsjha123"
print(abc)  
print("abc.lower()", abc.isalpha())  #return false

# 17. islower()- check whether the entire string is in lower case or not
print("abc.islower()", abc.islower())

# 18. isupper()- check whether the entire string is in upper case or not
print("abc.isupper()", abc.isupper())

# 19. isprintable()- if escape sequecne encounter that does not get print on console return false, else true
pr="you are a good boy\n"
print("pr has \\n, so: ", pr.isprintable())  #output-false

# 20. isspace()- return true only when string is completely composed of white spaces
sp='        '
print("sp: ", sp)
print("sp.isspace(): ", sp.isspace())
sp='        p'
print("sp: ", sp)
print("sp.isspace(): ", sp.isspace())

# 21. istitle()-return true only when the first letter of each word is capital and rest all are in lower case
tit="You Are AmAzing"
print("tit: ", tit)
print("tit.istitle(): ", tit.istitle())  #output-false

tit="You Are Amazing"
print("tit: ", tit)
print("tit.istitle(): ", tit.istitle())  #output-true

# 22. swapcase()- swap the lower case to upper case and upper case to lower case
swap="You Are Great, ThanKU"
print("Swap: ", swap)
print("Swap.swapcase(): ", swap.swapcase())

# 23. title()-capitalise the first letter of each word and convert other in lower case
lst='You are GooD, may God BlesS yoU'
print("lst: ", lst)
print("lst.title(): ", lst.title()) 
