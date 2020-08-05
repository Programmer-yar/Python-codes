                #Function returning values

def max(x,y):   # x , y are called function parameters
    if x>y:
        return x  #it will return a value in case the condition is true
    else:         
        return y


print(max(3,10))
#In max(3,10) 3 and 10 are aguments passed to function parameters x and y

z=max(4,5)
print(z)

# Returning a dictionary
"""
- A function can return any complex data structure including
  dictionary or list
"""

def build_person(first_name, last_name, age=""):

    person={'first':first_name,'last':last_name}

    if age:
        person['age']=age
        
    return person

print(build_person('ahmad','yar',25))
programmer=build_person('ahmad','yar')
print(programmer)

              # Using a function with while loop #

def get_formatted_name(first,last):
    full_name=first+' '+last        
#if comma is used in the above line as a seperator it will create tuple

    return full_name.title()

while True:
    print('Enter "q" and press enter to quit\n')
    
    f_name=input('enter your first name :')
    if f_name=='q':
        break
    
    l_name=input('enter your last name :')
    if l_name=='q':
        break

    formatted_name=get_formatted_name(f_name,l_name)
    print('\n Hello!',formatted_name)
