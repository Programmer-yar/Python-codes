                           #Lambdas
""" Normal function are first defined and then called
but in lambdas a function can be created and called at the same time
Functions created using lambdas are called anonymous functions"""

"""Normal functions can be used outside of a program or outside of a document
but lambda is limited to the program where it was declared
- lambdas can be called local functions while other functions are called
  global functions"""

#Lambdas are mostly used when passing a simple function as argument to another function

""" Just as strings and integers can be used without assigning them to variables
with lambdas functions can be used in the same way
"""
def my_func(f,arg):
    return f(arg)

print(my_func(lambda x:2*x*x,5))

"""
- lambdas are not as powerful as defined funtions
- but they can evaluate expressions which involve a single line of code
"""
#named function
def polynomial(x):
    return x**2+5*x+4
print(polynomial(-4))

#lambda
print((lambda x:3**x)(3))
print((lambda x,y: x**2+5*y+4)(-4,5))

double=(lambda x: x*2)
print(double(3))

#
triple = lambda x:x*3
add = lambda x,y:x+y
print(add(triple(3),4))
