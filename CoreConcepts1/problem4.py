import os

directory_path='/'

# list all files and directories
contents=os.listdir(directory_path);

# print each file and directory
for item in contents:
    print(item)