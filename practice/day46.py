# os module- Operating System
import os
# if (not os.path.exists("Event")):
#     os.mkdir("Event")
# for i in range(1, 101):
#     file_name="main.py"
    
#     file2="tutorial.md"
#     dir=f"Event/task{i}"
#     if not os.path.exists(dir):
#         os.mkdir(dir)
#     open(os.path.join(dir, file_name), "w").close()
#     os.path.join(dir, file2)

print(os.stat("day46.py").st_size)
print(os.stat("day46.py"))