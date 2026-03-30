import time
n=int(input("Enter the Number of Rows: "))
print("Printing Sqaure Pattern...")
time.sleep(3)
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

     
print("Printing Increasing Triangle Pattern...")
time.sleep(3)
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()


print("Printing Decreasing Triangle Pattern...")
time.sleep(3)
for i in range(n):
    for j in range(i, n):
        print("*", end=" ")
    print()


print("Printing Right Increasing Triangle pattern...")
time.sleep(3)
for i in range(n):
    for j in range(i, n):
        print(" ", end=" ")
    for k in range(i+1):
        print("*", end=" ")
    print()


print("Priting Upward Hill Pattern...")
time.sleep(3)
for i in range(n):
    for j in range(i, n):
        print(" ", end=" ")
    for k in range(i+1):
        print("*", end=" ")
    for l in range(i):
        print("*", end=" ")
    print()

    
print("Printing Right Decreasing Triangle pattern...")
time.sleep(3)
for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for k in range(i, n):
        print("*", end=" ")
    print()

 
print("Priting Downward Hill Pattern...")
time.sleep(3)
for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for k in range(i, n):
        print("*", end=" ")
    for l in range(i, n-1):
        print("*", end=" ")
    print()
