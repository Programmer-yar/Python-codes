import random        #importing a module

for number in range(5):
    value=random.randint(1,6)
    print(value)
    
from math import pi, cos # importing only 2 function from math module
print(pi)               # i.e pi and cos
print(cos(90))

#Using 'as' to give function a different name or alias

from math import sqrt as square_root #importing a specific function under
print(square_root(100))              #different name


#Importing all functions in a module
from math import *

