                              #List and tuple Slices
"""More advanced method of getting data from lists
lists are indexed using two colon seperated integers.
This method returns the list between the indices in square brackets"""

squares=[0,1,4,9,16,25,36]
print(squares[1:2])
print(squares[2:5])
#first index included in result but second is not

#Effect of omitting 1st and 2nd index
nums=[2,4,6,8,12,15]
print(nums[:2])
print(nums[2:])

t_tuple=('my',1,'your',2)
print(t_tuple[:1])

"""   Using 3rd argument in list slicing  """
""" [start:stop:interval] """
#3rd argument specifies the interval
random=[1,2,5,7,8,9,10,13,16,17,19,22]
print(random[1:8:2])
print(random[::2])  #prints alternate values
print(random[::1])  #prints all values


