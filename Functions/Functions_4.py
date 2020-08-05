          #Passing  an arbitrary number of arguments

"""
- the parameter ' *toppings ' collects as many arguments as calling
  function provides
"""
def make_pizza(*toppings):
    print('Making a pizza with')

    for topping in toppings:
        print('-',topping)

make_pizza('extra cheese')
make_pizza('mushrooms','olives','bar-b-que')
"""
- The function make_pizza stores arguments in a tuple
"""
###############################################################

           #Mixing Positional and Arbitrary Arguments
"""
A function that accepts several different types of arguments
arbitrary arguments must be placed in last
"""
def makes_pizza(size, *toppings):

    print('Making the ' + str(size)+'-inch pizza' ,
          'with toppings as follows')

    for topping in toppings:
        print('-', topping)

makes_pizza(16, 'extra cheese')
makes_pizza(12, 'pepproni', 'olives', 'mushrooms')

################################################################

                   #Using arbitrary keyword arguments
"""
- a function that accepts as many key:value pairs as the calling
  function gives
"""

"""
In the below function
the parameter " **user_info  " allows python to create an empty dictionary
and pack whatever name:value pair it recieves

the function "build_profile" expects first and last name and then allows
user to pass as many key value pairs as they wish to
"""

print('\nThe function with arbitrary keyword arguments " ** "\n')

def build_profile(first, last, **user_info):

    
    profile={}
    profile['first name']=first
    profile['last name']=last

    for key, value in user_info.items():
        profile[key]=value

    return profile

user_profile=build_profile('albert', 'einstein',
                           location='princeton',
                           subject='physics')
print(user_profile)
