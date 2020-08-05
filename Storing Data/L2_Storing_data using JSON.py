import json

user_name=input("What is your name")
file_name="user_name.json"

with open(file_name,'w') as file:
    json.dump(user_name, file)
    print("We will remember you",user_name)
