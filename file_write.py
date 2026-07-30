# writing with python 

txt_data = "I LOVE PIZZA!!!"

file_path = "outout.txt"

with open(file_path, "w") as file:
    file.write(txt_data)
    print(f"Text File '{file_path}' Was Created  ")