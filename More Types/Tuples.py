                            #Tuples 
""" are similar to lists but immutable(can not be changed).
    are faster than lists.
    they are created using parenthesis instead of square brackets. """
words=('orange', 'blue', 'yellow',123)
print('The tuple named words\t',words)
print('0th element\t',words[0])
print('3rd element\t',words[3])

#Tuples can be created without parenthesis

my_tuple='lake','blue', 341
print('A tuple created without parenthesis\t',my_tuple,'\nthe 2nd element\t',my_tuple[2],'\n')

#Tuples can be overwritten
words=('guava','banana','paint',23)
print('Overwritten Tuple words\t',words)

#tuples can be nested just like lists and dictionaries
nest_tuple=('orange',(0,0,245),'blue',123)
print('A nested tuple\t',nest_tuple,'\n accessing its 1st element',nest_tuple[1])

#empty tuple
kg=()
print('An empty tuple\t',kg)
#immutable
print('An error will occur when you try to change a tuple element')
words[1]=words[2]
