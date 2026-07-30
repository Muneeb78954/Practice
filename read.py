# txt
file_path = "C:/Users/TARAR COMPUTER/Desktop/Python Projects/File detection/outout.txt"
try:
    with open(file_path, "r") as file:
        content = file.read()

    print(content)
except FileNotFoundError:
    print("File Not Found!")
except PermissionError:
    print("You do not have permission to read this file!")

# JSON 
import json 

file_path = "C:/Users/TARAR COMPUTER/Desktop/Python Projects/File detection/outout.json"
try:
    with open(file_path, "r") as file:
        content = json.load(file)

    print(content)
except FileNotFoundError:
    print("File Not Found!")
except PermissionError:
    print("You do not have permission to read this file!")

# CSV 
import csv

file_path = "C:/Users/TARAR COMPUTER/Desktop/Python Projects/File detection/outout.csv"
try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)
except FileNotFoundError:
    print("File Not Found!")
except PermissionError:
    print("You do not have permission to read this file!")