                   #Decorators part (ii)

""" Checking the input and output of a function using decorators"""

def verbose(f):
    def r(x):
        y=f(x)
        print ( "called with argument ",x)
        print("returned ",y)
        return y
    return r

#every call of f will print what was entered and returned in f... eg

@verbose
def s(x):
    return x**2

print(s(3))
