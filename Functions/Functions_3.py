                 #Passing list as argument to a function

def greet_users(users):

    for user in users:
        print('Welcome,',user.title(),'!')

names=['ramay','ahmad','haris']
greet_users(names)

#################################################################

               #Modifying a list within a function
def print_models(unprinted_models, printed_models):

    

    while unprinted_models:               #Another lengthy method ---for model in range(len(unprinted_models)):---
        
        current_model=unprinted_models.pop()
        print('The model',current_model.title(),'has been printed')
        printed_models.append(current_model)


def complete_models(printed_models):
    print('The following models have been printed')
    
    for model in printed_models:
        print(model)

to_make=['iphone','samsung','3d cat']
made=[]

print_models(to_make, made)
complete_models(made)
"""
- if you do not want the original list to be modified send a copy using
the command === 'print_models(to_make[:],made)' ===
- it is more effecient to use original lists and will also save the time
"""



