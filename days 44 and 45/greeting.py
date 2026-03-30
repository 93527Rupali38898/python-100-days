def welcome(user="user"):
    print(f"Have a good day, dear {user}")
def sum(a=2, b=2):
    print(f"{a}+{b}={a+b}")
    
    
fact="The sun rises in the east"
# importing this directly will lead to unexpected behavior, as the code written in welcome(), sum() and fact will get executed, even if we have not imported anything and we don't want this (we want that the function that are imported only that got executed)
'''
welcome()
sum()
print(fact)
'''
print(__name__)
if __name__=="__main__":
    welcome()
    sum()
    print(fact)

