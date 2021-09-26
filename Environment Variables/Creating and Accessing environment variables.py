"""
Windows:
First we need to create environment variables in windows
1- Go to My computer icon Properties by right clicking
2- In the top left side click on "advanced system settings"
3- click on "environment variables" and create "User variables".
"""
"""
Ubuntu/linux:
Create environment variables in "/etc/environment" file.
1- Open "/etc/environment" using "vim" or "nano" editor as you like
2- store variable: <variable_name>="<value>"
3- Restart ubuntu or logout and login back
"""
"""
To access the environment variables follow the following method
"""

import os

test_id = os.environ.get('test_id')
#USER_ID was already defined as environment variable
#get method used in "dictionaries" to get 'value' of a 'key'
user_password = os.environ.get('test_pass')
test_var = os.environ.get('test_var')
test_var1 = os.environ.get('test_var1')
DEBUG = os.environ.get('DEBUG')

# print("test_id", test_id)
# print("test_pass" ,user_password)
# print("test variable: ", test_var)
# print("test variable 1: ", test_var1)
print(eval(DEBUG))
print(type(DEBUG))