my_dict = {'a': 1, 'b': 2}
print(my_dict.get('a'))        # Output: 1
print(my_dict.get('c', 'N/A')) # Output: N/A

l=[]
num1=int(input("Enter the number 1: "))
l.append(num1)
num2=int(input("Enter the number 2: "))
l.append(num2)
num3=int(input("Enter the number 3: "))
l.append(num3)
num4=int(input("Enter the number 4: "))
l.append(num4)
max=l[0]
for number in l:
    if (number>max):
        max=number
print("maximum number is: ", max)


l=['make a lot of money', 'buy now', 'click this', 'subscribe this']
comment=input("Enter your comment: ")
for spam_word in l:
    if spam_word in comment:
        print("Your Message is Spam")
        break
else:
    print("Thanku for Your comment")


i=1
while(i!=51):
    print("Value is:", i)
    i=i+1

color=['red', 'green', 'blue', 'violet', 'black', 'white', 'pink', 'yellow']
color_updated=[word.capitalize() for word in color]
print(color_updated)
lenght=len(color_updated)
print(lenght)
i=0
while(i!=lenght):
    print(f'Item at {i} index is: {color_updated[i]}')
    i=i+1

for i in range(4):
    print(i)
    if (i==2):
        continue

# Question 1: write a multiplication table of a number entered by user using for loop
num=int(input("Enter the number for multiplication table: "))
for i in range(1, 11):
    print(f"{num} X {i} = {num*i}")
    

# Question 2: Write a program to greet to all the person name stored in the list
# and whose name start with s
l1=['harry', 'sohan', 'sachine', 'rohan']
l1=[word.title() for word in l1]
for name in l1:
    if (name.startswith('S')):
        print(f"Hello, {name}!")
        
# Question 3: attempt problem using while loop
num=int(input("Enter the Number for Multiplication table: "))
i=1
while(i!=11):
    print(f"{num} X {i} = {num*i}")
    i+=1

# Question 4: Write a program to find whether a given number is prime or not
import math
num=int(input("Enter the number you want to check for prime: "))

if (num>0):
    max_divide=int(math.sqrt(num))
    count=0
    i=2
    while(i!=(max_divide+1)):
        if (num%i==0):
            count+=1
            
            break
        i+=1
    if (count==0):
        print(f'{num} is a prime number')
    else:
        print(f'{num} is not a prime number')
else:
    print("We can't define Negative number as prime or non prime")

# Question 5: Write a program to find the sum of first natural number using while loop
num=int(input("Enter the number till you want the sum: "))
sum=0
i=1
while(i<=num):
    sum+=i
    i+=1
if (sum==0):
    print("Negative number Entered...")
else:
    print(f'Sum of first natural number till {num} is {sum}')

# Question 6: Write a program to calculate the factorial of a given number using for loop
num=int(input("Enter the number you want to factorial: "))
fact=1
for i in range(num, 1, -1):
    fact*=i
if (num<0):
    print("Factorial of {num} is undefined!!")
else:
    print(f'Factorail of {num} is: {fact}')

# Question 7: Write a profram to print the folowing start patten
'''        *
        *   *   *
    *   *   *    *   *'''
row=int(input("Enter the number of row you want for hill pattern: "))
if (row<=0):
    print("Invalid number of row!!!!")
else:
    for i in range(row):
        for j in range(i, row-1):
            print(' ', end=' ')
        for k in range(i+1):
            print('*', end=' ')
        for l in range(i):
            print('*', end=' ')
        print()
            
    
# Question 8: Write a program to print the followinf start Pattern
'''*
    * *
    * * *'''
row=int(input("Enter the number of row for increasing triangle: "))
if (row<=0):
    print("Invalid number of row")
else:
    for i in range(row):
        for j in range(i+1):
            print('*', end=' ')
        print()

# Question 9: Write a program to print the followinf start Pattern
'''* * *
    *   *
    * * *'''
row=int(input("Enter the number of row: "))
if (row<=0):
    print("Invalid number of row")
else:
    for i in range(row):
        for j in range(row*2 - 1):  # Total number of columns for a symmetric pattern
            if (i == 0 and j % 2 == 0) or (i == 1 and (j == 0 or j == row*2-2)) or (i == 2 and j % 2 == 0):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()  

# Question 10: Write a program to print multiplication table of n using for loop in reversed order
num=int(input("Enter the number for reverse multiplication table: "))
if (num<=0):
    print('Invalid number for multiplication table')
else:
    for i in range(10, 0, -1):
        print(f'{num} X {i} = {num*i}')



num=[1,2, 3, 5, 6]
for i in num:
    print(i)
    if (i==5):
        continue
else:
    print("Exit without break statement")