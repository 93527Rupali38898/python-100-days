# time module 
import time

def forLoop():
    print("For Loop")
    for i in range(600000):
        # print(i)
        pass
def whileLoop():
    i=0 
    print("While Loop")
    while(i<600000):
        # print(i)
        i=i+1
        pass
print("1. time.time()")
init1=time.time()
forLoop()
print(f"The time for loop took is {time.time()-init1:.4f} sec")
init2=time.time()
whileLoop()
print(f"The time while loop took is {time.time()-init2:.4f} sec")


print("2. time.sleep()")
for i in range(5):
    print(i)
    time.sleep(1)

print("3. time.localtime()")
local=time.localtime()
print(local)
print(type(local))


print("4. time.strftime()")
format=time.strftime("%Y-%m-%d %H:%M:%S", local)
print(format)

