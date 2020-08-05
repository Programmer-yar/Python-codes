                             #Map & Filter
""" Built-in functions
- map takes a function and list/iterable as argument
- returns list/iterable with function applied to each element in list/iterable
"""

def mult(x):
    return x*2

nums=[2,3,4,5,6]
result=list(map(mult, nums))  #using list command converts the result into list
print(result)

#using lambda
result=list(map(lambda x:x**2,nums))
print(result)

""" Filter
- this function removes the iterable that do not fullfil a condition
or prediction """
numb=[11,22,33,44,55]
res=list(filter(lambda x:x%2==0,numb))
print(res)

nums=[1,4,5,6,7]
left=list(filter(lambda x:x<5,nums))
print(left)
