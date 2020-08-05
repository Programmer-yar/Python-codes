                         #FUNCTIONAL PROGRAMMING
#Programming based around functions
"""  High Order Functions - take other functions as arguments or
     return them as results """

def apply_twice(func,arg):
    return func(func(arg))

def add_five(x):
    return x+5

print(apply_twice(add_five,10))
#func(func(arg))=add_five(add_five(10))=add_five(15)=20


def test(func, arg):
  return func(func(arg))

def mult(x):
  return x * x

print(test(mult, 2))
