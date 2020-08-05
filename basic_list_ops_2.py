                            #Basic list Operations part(2)

names=['ahmad','ramay','bhutta','arsi','usman']
nums=[1,4,2,9,8,3]

#Copying lists
cop_names=names #This method is false and causes ammendment problems
copy_names=names[:]

print('The original list names is\t',names)
print('The original list nums is\t',nums)


#removing an item by value
rem_val1='arsi'
names.remove('arsi') #this command only deletes one occurance
print('After removing "arsi" by using remove',names)
print('the name ',rem_val1.title(),'is not an authentic')

#simple list reversal
names.reverse()
print('\nafter permanantly reversing list order',names)


#Temporary sorting of lists using 'sorted()' method
print('\ntemporary sorted names list is\t',sorted(names))

#Temporary reverse sorting
print('\ntemporary sorted reverse ordered names list is\n',sorted(names,reverse=True))
print('original list is\t',names)

#Permanent sorting of lists using 'sort()' method
names.sort()
nums.sort()
print('\npermanantly Sorted nums list',nums)
print('Permanantly Sorted names list',names)
print(nums)

#finding length of list
print(len(names),len(nums))

#reverse permanant sorting
names.sort(reverse=True)
print('\n Sorted in reverse order',names)



