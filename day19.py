#                         break and continue statement
# break- skip a part of code
for i in range(1, 11): #to get value till 10 as it iterate till n-1
    if (i==7):
        break
    print("Value of i is:", i)
# entire code get exited due to break statement
print()
# continue- to skip a particular iteration and then continue after that
for i in range(1, 11): #to get value till 10 as it iterate till n-1
    if (i==7):
        continue  
    print("Value of i is:", i)  #only 7 will not get printed
