# readline and writeline 
# creating a file
try:
    f=open("file50.txt", "x")
except:
    print("File already exists")
    
# using readline to read the marks in student

f=open('file50.txt', 'r')
i=0
while True:
    i=i+1
    line=f.readline() # readline is used to read the file line by line
    if not line:
        break
    m1=line.split(",")[0]
    m2=line.split(",")[1]
    m3=line.split(",")[2]
    print(f"Type of m1:{m1} is {type(m1)}")
    print(f"Type of m1:{m2} is {type(m2)}")
    print(f"Type of m1:{m3} is {type(m3)}")
    print(f"Marks of {i} student in Maths is {m1}")
    print(f"Marks of {i} student in Science is {m2}")
    print(f"Marks of {i} student in English is {m3}")
    # print("\n\n")
    
    
    
# WRITELINES IN FILE METHOD
lst=["red", 'green', 'blue', 'yellow', 'orange', 'purple']
color=[x.capitalize() for x in lst]
with open("file50-writeline.txt", 'w') as fw:
    for x in color:
        fw.writelines(x+"\n")