import os

file_path = "C:\\Users\\TARAR COMPUTER\\Desktop\\hidden\\hide.txt"

if os.path.exists(file_path):
    print(f"The Location '{file_path}' exits")
else:
    print("The Location not exist!")


if os.path.isfile(file_path):
    print("This is a file")
elif os.path.isdir(file_path):
    print("This is a direcctory")
else:
    print("It is a directory")
