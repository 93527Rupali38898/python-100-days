#  seek(), tell() and truncate() functions
# seek() function is used to move the file pointer to a specific location in the file.
# tell() function is used to get the current position of the file pointer in the file.
# truncate() function is used to truncate the file to a specific size.

# Example of seek() function
with open("file.txt", "r") as f:
    f.seek(10)  # Move the file pointer to the 10th byte in the file
    data = f.read(5)  # Read the next 5 bytes from the file
    print(data)  # Output: "world"

# Example of tell() function
with open("file.txt", "r") as f:
    f.seek(10)  # Move the file pointer to the 10th byte in the file
    position = f.tell()  # Get the current position of the file pointer
    print(position)  # Output: 10

# Example of truncate() function
with open("file.txt", "r+") as f:
    f.truncate(10)  # Truncate the file to theff