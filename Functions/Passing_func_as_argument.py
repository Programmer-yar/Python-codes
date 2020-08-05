def add(x,y):
    return x+y

def do_twice(func,x,y):
    return func(func(x,y),func(x,y))

print(do_twice(add,5,6))
