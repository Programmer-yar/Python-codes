                            #Basic list Operations
#collection of items in a particular order
nums=[2,10,4,5,6]
names=['ahmad','yar','name','place','who am i']

#accessing elements
print(nums[2])
print(names[0].title()) #'title()' capitalize first letter of every word after a space

#[-1] in index represent the last value while '-2' will give 2nd last and so on
print('My question is',names[-1])
print('My name is '+names[0].title())
print(nums[-2])

#adding elements to the last of list
nums.append(7)
names.append('ego')
print('after adding an element to the end using append\n',nums)
print('after adding an element to the end using append\n',names)

#removing element of a list using del
del nums[1]
del names[3]
print('after removing 1st element using del\n',nums)
print('after removing 3rd element using del\n',names)

#removing element of a list using pop()
"""Removes last item and also allows you to work on that element
- treats list as a  stack in which last item is considered to be on top"""
pop_num=nums.pop()
print('nums list after popping\t',nums,'\npopped element is',pop_num)
pop_name=names.pop()
print('nums list after popping\t',names,'\npopped element is',pop_name)

#Popping item from any position using pop
print('nums list before poping 2nd element\t',nums)
pop_num2=nums.pop(2)
print('nums list after popping 2nd element\t',nums,'\npopped element is',pop_num2)

print('names list before poping 1st element\t',names)
pop_name1=names.pop(1)
print('nums list after popping 1st element\t',names,'\npopped element is',pop_name1)
