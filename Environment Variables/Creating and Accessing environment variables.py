"""
First we need to create environment variables in windows
1- Go to My computer icon Properties by right clicking
2- In the top left side click on "advanced system settings"
3- click on "environment variables" and create "User variables"
"""
"""
To access the environment variables follow the following method
"""

import os

user_id = os.environ.get('USER_ID')
#USER_ID was already defined as environment variable
#get method used in "dictionaries" to get 'value' of a 'key'
user_password = os.environ.get('user_password')

print(user_id)
print(user_password)
