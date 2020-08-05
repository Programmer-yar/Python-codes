#remember strings are essentialy lists in python
name='Happy as ever'
print(name[::-1])

"""   Using negative values in list slices  """
#-ive values count from the end of the list
#special practice and understanding required

random=[1,2,5,7,8,9,10,13,16,17,19,22]
#as we have given -ive interval, the program assumes negative initial limit i.e
#starting from end
print(random[:1:-1])
print('''\n You should see [] because interval is positive going forward while limit
  is negative that is going backward''')
print(random[-1:4])
print(random[2:-3])
print('\n you should see empty list here')
#while using negative step also reverse limit otherwise output will be []
print(random[1:7:-1])
#like this
print(random[7:1:-1])

print(random[1:-1])
print(random[-1:1])
print(random[-1:1:-1])
