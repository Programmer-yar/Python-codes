flow='y'
print('welcome to a simple calculator\n You can perform "*"  "/"\n "+"   "-"')
print('OPerations')

while flow=='y':
    x=float(input('Please enter the first number'))
    y=float(input('Please Enter the 2nd number'))
    print('Enetr a sign out of the following')
    print('+ (add)   - (minus)   / (division)   * (multiply) ')
    z=input('Enter the operation here\n')
    if z=='+':
        print(x+y)
    elif z=='-':
        print(x-y)
    elif z=='*':
        print(x*y)
    elif z=='/':
        print(x/y)
    else:
        print('invalid operation')
    print('do u want to perform another operation?/n 1)Y/y   2)N/n')
    flow=str(input())
