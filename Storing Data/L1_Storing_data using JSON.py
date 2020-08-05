          #Storing user data even when the program is closed
"""
JSON <--> Java Script Object Notation
- Share data between different Python programs and other languages programs
- Uses 'json.dump(data, file_name/path)' and 'json.load( file_name/path )' metods
"""
import json

numbers=[1,2,3,7,8,9]
file_name='numbers.json'
with open(file_name, 'w') as file:
    json.dump(numbers, file)

with open(file_name) as file:
    numbers=json.load(file)
    
print(numbers)

"""---------------------------Next Part----------------------------------"""
print("\n")

try:
    with open('user_name.json') as file_1:
        name=json.load(file_1)
        

except FileNotFoundError:
    name=input("Enter your name")
    with open('user_name.json', 'w') as new_file:
        json.dump(name, new_file)
    
else:
    print("welcome back", name)


