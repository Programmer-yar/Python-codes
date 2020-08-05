                            #Functions

#Functions seperate blocks of code from main program

def greet_user(user):      # user is function parameter
    print('Welcome',user)

"""
Arguments are pieces of information which the funtion needs
to work
"""

"""
In the below function call 'ahmad' is passed as argument to function parameter
'user'
"""
print(greet_user('ahmad'))

############################################################
    
                       #Function call methods
#Positional arguments (order of arguments matters in this method)

""" In this method a function is called by simply passing the arguments in order to
    defined parameter"""
def my_name(first, last):
    print('Your name is',first.title(),last.title(),'\n')


#if position of arguments is changed it will give different result with positional arguments
my_name('yar','ahmad')   
my_name('wajahat','hussain')


#Keyword arguments (order of arguments does not matter)
""" this method tells python which parameter should be matched with
    given argument"""
my_name(first='wajahat',last='hussain')
my_name(last='yar',first='ahmad')

##########################################################################

              #Using default value for a parameter while defining function

def pet(name,pet_type='dog'):
#Non-default parameter always comes first
    
    print("\nyour pet type is",pet_type.title())
    print('Its name is',name.title())

pet(name='poni')  #In this call it will take value of pet_type parameter as dog which is by default

pet(pet_type='cat',name='mano')
"""In the above function call default value of 'pet_type' will be overwritten by argument cat"""

###########################################################################

                        #Argument Optional
"""If user wants to provide additional information then he can use optional argument"""

def user_name(first,last,middle=""):
    print('\nthe user name is',first.title(),middle.title(),last.title())

user_name('muhammad','yar','ahmad')
user_name('muhammad','yar')




    
