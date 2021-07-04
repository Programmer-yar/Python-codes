prime={1:2,2:3,3:5,5:6}
print(prime[prime[3]])

"""Finding keys in dictionary"""
serial={1:'one',
        2:'two',
        3:'three',
        '4':'four'}
print(1 in serial)
print(4 not in serial)
print('4' in serial)

#get method for dictionaries
"""Same as indexing but returns None or argument satatement
if key is not found"""

num={"orange":[2,3,4],
     "apple":"fruit",
     234:432}
print(num.get('orange'))
print(num.get(234))
print(num.get(432))
print(num.get('blue', "not present"))

fib = {1: 1, 2: 1, 3: 2, 4: 3}
print(fib.get(4, 0) + fib.get(7, 5))
