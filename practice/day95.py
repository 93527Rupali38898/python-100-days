# Regular Expression
import re
pattern1="[abc]"
text1="abcdefgh"
match1=re.findall(pattern1,text1)
print(match1)

pattern2="^abc"
text2="abcdefgh"
match2=re.search(pattern2,text2)
print(match2)

pattern3="abc$"
text3="rupaliakjbcd"
match3=re.search(pattern3, text3)
print(match3)
if match3:
    print("yes")
else:
    print("no")
    
    

pattern4="c.t"
text4="raju and cat are walking"
match4=re.search(pattern4, text4)
print(match4)

patter5="colou?r"
text5="color and colour sounds same. and also color"
match51=re.findall(patter5, text5)
match52=re.search(patter5, text5)
print(match51)
print(match52)


pattern6="cat|dog"

text6="cat and dog are walking"
match6=re.findall(pattern6, text6)
match62=re.search(pattern6, text6)  
print(match6)
print(match62)


pattern7="cat+"
text71="cat is very cute"
text72="dog is very cute"

match71=re.search(pattern7, text71)
match72=re.search(pattern7, text72)
print("cat", match71)
print("dog",match72)

pattern8="ca*"
text81="car cat"
text82="dog and "
print(f"presence:{re.search(pattern8, text81)}")
print(f"ansence:{re.search(pattern8, text82)}")


pattern9="ca+"
text91="car cat"
text92="dog and "
print(f"presence:{re.search(pattern9, text91)}")
print(f"absence:{re.search(pattern9, text92)}")


