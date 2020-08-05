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

def get_new_username():
    user_name=input("what is your name")
        file_name='name_store.json'
        with open(file_name, 'w') as file:
            json.dump(user_name, file)
    return user_name

def greet_user_r():
    """ Simply greets user """
    user_name=get_stored_username()
    
    if user_name:
        print("Welcome back", user_name.title())

    else:
        name=get_new_username()
        print("we will remember you", name, "!")
            
greet_user_r()
