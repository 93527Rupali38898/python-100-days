# rock, paper and scissor
import random
lst=[0, 1, 2] #rock, paper, scissor
comp=random.choice(lst)
print(comp)

print("Welcome to Rock, Paper and Scissor Game!!")
print("Enter number as your response: ")
print("0 for Rock: ")
print("1 for Paper")
print("2 for Scissor")
user=int(input("Enter your Choice: "))
print("Enter any other number to exit...")
while(user==0 or user==1 or user==2):
    if(user==comp):
        print("Draw")
    elif ((user==0 and comp==1) or (user==1 and comp==2) or (user==2 and comp==0)):
        print("You Lose")
        print("Better Luck Next Time!!")
    else:
        print("Hurrah!! You Win")
    user=int(input("Enter your Choice: "))