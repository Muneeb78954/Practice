# writing with python 
# Text Files
txt_data = "I LOVE PIZZA!!!"

file_path = "outout.txt"
try:                            # w-> overrride the data | x-> give error if already exist 
    with open(file_path, "x") as file:
        file.write(txt_data)
        print(f"Text File '{file_path}' Was Created  ")
except FileExistsError:
    print("This file already exist")
    

"""For List"""
employees = ["Elon Musk", "Bill Gates", "Larry Page"]

try:                            # w-> overrride the data | x-> give error if already exist 
    with open(file_path, "x") as file:
        for employee in employees:
            file.write(employee + "\n")
        print(f"Text File '{file_path}' Was Created  ")
except FileExistsError:
    print("This file already exist")
