#                     create a program to greet user according to time
import time
name=input("Enter your name: ")
name1=name.title()
struct_time=time.localtime() #using this as it seems to be most appropiate
hour=struct_time.tm_hour
print("Hour on You pc is:", hour)
if (hour>=5 and hour <12):
    print("Good Morning", name1)
    print("Have a Nice day", name1, "!!")
elif (hour>=12 and hour<17):
    print("Good Afternoon", name1)
    print("I hope so You are Completing Your Tasks !!")
elif (hour >=17 and hour <21):
    print("Good Evening", name1)
    print("It's Tea Time", name1, "!!")
else:
    print("Good Night", name1)
    print("Sweet Dreams", name1, "!!")
    