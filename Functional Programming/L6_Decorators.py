                               #Decorators
"""
- Modify functions using other functions
- extends the functionality of original function without modifying it """

def decor(func):
    def wrap():
        print('============')
        func()
        print('============')
    return wrap

def decor1(func):
    def wrap1():
        print('***********')
        func()
        print('***********')
    return wrap1

def print_text():
    print('Hello World')

decorated=decor(print_text)
decorated()

print_text=decor(print_text)
print_text()

#Wrap a function in a decorator by pre-pending the function definition with

@decor     # @ symbol and decorator name
#this replaces decorated=decor(print_text) or print_text=decor(print_text)
@decor1
def print_text():
    print('Hello Python')

print_text()


