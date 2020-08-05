                          #Pure Functions
# FP makes use of pure functions
""" Pure Functions
- Return a value that only depends on arguments
- e.g cos(x) for same value of x will always give same value
- easy to reason and test
- output for a same input can be stored for future refrence
  and thus reducing function calling. This process is called memoization
"""
#Memoization- Stores the result of expensive function calls
# and returns cached result when some input occurs again
# Optimization technique to speed up computer programs

def pure_func(x,y):
    temp=x+2*y
    return temp/(2*x+y)

"""  Impure Functions
- will always give a different result even for same value of argument
- will always cahnge parameters
"""
some_list=[]

def impure(arg):
    some_list.append(arg)
