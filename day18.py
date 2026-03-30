#               while loop, do while loop and else clause with while loop
# while loop execute the code block till the condition is True
# syntax of while loop : while condition: 

i=10
while i>0:
    print(i)
    i-=1
    
# infinite while loop
"""while True:
    print("Infinite Loop")
    """

# use cases of while Loop:
# taking user input for a particualr task and we don't know the number of iteration
while True:
    password=int(input("Enter the Password: "))
    if (password != 1234):
        print("Invalid Password, Try Again!!")
    else:
        break
print("Sir, Here is Your Information")


# using else with while loop:
'''NOTE -else is execute after the while loop, 
if the loop is "NOT" terminated with break statement'''

i=0
while i<10:
    i+=1
    print(i)
else:
    print ("Loop Exited without Break Statement")
    # this line get executed

i=1
while i<15:
    print(i)
    i+=1
    if (i==10):
        break
else:  #this will not get executed as the loop get terminated by break statement
    print("Print statement in while loop")
    
    
#                            do-while loop (Exit- Controlled Loop)
# do-while loop are a kind of loop that will execute atleast once regradless of condition
# python does not support do-while directly, but we can emulate it using the concept of:-
# infinite while loop with break statement
'''
while True: 
    code 
    if not condition: 
        break'''

# example:- this work as do-while loop
while True:
    num=int(input("Enter the Value of Num (greater than 10): "))
    if num>10:
        print("Your Entered Number is:", num)
        print("Thank You!!")
        break
    
    print("Try Again")