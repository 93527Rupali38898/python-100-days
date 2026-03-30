# how to create and perform task on file in python 


# READING A BINARY FILE
# f=open("C:\\Users\\LENOVO\\Desktop\\suhani.jpg", "rb")
# text=f.read()
# print(text)
# f.close()



# CREATING A FILE USING create mode(x)
# for creating applying a try again as it throws an error if the file already exists
try:
    f=open("file49.txt", "x")
    f.close()
except:
    print("File already exists")

# WRITING IN A FILE
fw=open('file49.txt', 'w')
fw.write("Hello, My Name is Rupali Goyal, I am currently in 3rd year, learning python to grow my career in the field of data science")
fw.close()

# READING A FILE
f=open('file49.txt', 'r')
text=f.read()
print(text)
f.close()

# APPENDING DATA IN THE FILE
f=open("file49.txt", "a")
data="hello this is new line added by append"
f.write(data)
f.close()


# reading again after appending

f=open('file49.txt', "r")
text=f.read()
print(text)

# NOTE:
# If we forget to close a file, two main problems can occur:
# 1. Data may remain in the buffer and may not get written to the file properly.
# 2. It can cause a resource leak (file handle/memory leak), which may crash the program.

# To avoid this, we use the 'with' keyword, which automatically closes the file after the block is executed, even if an error occurs.
print("\nWith keyword\n")
with open("file49.txt", 'r') as fr:
    print(fr.read())