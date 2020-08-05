                              #Refactoring
""" Breaking a code into a series of functions that has specific jobs """
""" Breaking a big problem into a series of small problems """

import json

#All in one function
def greet_user():
    """ Greets user by name """
    
    file_name='name_store.json'
    try:
        with open(file_name) as file:
            user_name=json.load(file)

    except FileNotFoundError:
        user_name=input("Enter your name")
        with open(file_name, 'w') as file:
            json.dump(user_name, file)
        print("You are in our good books from now")

    else:
        print("Welcome back!", user_name)
        

greet_user()

#Refactoring
def get_stored_username():
    """ Gets username if already stored in json file """
    file_name='name_store.json'

    try:
        with open(file_name) as file:
            name=json.load(file)

    except FileNotFoundError:
        return None

    else:
        return name

def greet_user_r():
    """ Simply greets user """
    user_name=get_stored_username()
    if user_name:
        print("Welcome back", user_name.title())

    else:
        user_name=input("what is your name")
        file_name='name_store.json'
        with open(file_name, 'w') as file:
            json.dump(user_name, file)
            print("we will remember you", user_name, "!")
            
greet_user_r()
