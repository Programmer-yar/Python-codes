                         #List Comprehension
"""quickly creates list which follow a general rule"""

squares=[var**2 for var in range(5)]
print(squares)
math=[i*2 for i in range(10)]
print(math)
a=[i for i in range(20) if i%3==0]
print(a)

a=[x*10 for x in range(5,9)]
print(a)

#Memory error
#this command when executed occupy 50% memory
test=[i for i in range(10**100)]

