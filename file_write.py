# writing with python 
# Text Files
import json 

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

# JSON FILE

file_path = "outout.json"

students = {
    "name" : "Muneeb",
    "age" : 20 ,
    "job": "Programmer"
}

try:                            # w-> overrride the data | x-> give error if already exist 
    with open(file_path, "w") as file:
        json.dump(students, file, indent=4) 
        print(f"Json File '{file_path}' Was Created  ")
except FileExistsError:
    print("This file already exist")

# CSV FILES
import csv
file_path = "outout.csv"

customers = [["name", "age", "job"],
             ["Elon Musk", 56, "Compuer Engineer"],
             ["Mark ZukerBerg", 32, "Software Engineer"],
             ["Bill Gates", 78, "CEO of Microsoft"]]

try:                            # w-> overrride the data | x-> give error if already exist 
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in customers:
            writer.writerow(row)
        print(f"CSV File '{file_path}' Was Created  ")
except FileExistsError:
    print("This file already exist")