                             #Dictionaries part 3
#Looping through dictionaries
user_0={'username':'mbzRamay','first':'Muhammad','last':'ramay'}

"""
- In the below for loop:
- key, value represent variables and can be named k,v or anything else
- .items() is a method for returning key:value pairs in a dictionary"""
for key,value in user_0.items():
    print('\nKey :',key,'\nValue :',value)


#Another example
fav_lan={'ahmad':'python','mudassir':'c#','haris':'swift'}
for name,language in fav_lan.items():
    print('\nName :',name.title(),'\nLanguage :',language.title())


#Looping through keys only, in a dictionary
""" keys() method will give keys only"""
print('\nPrinting keys with keys() method')
for names in fav_lan.keys():
    print(names.title())


#Looping through keys without using keys() method
"""Looping through keys is default behaviour of looping through dictionaries
- the above code can be re-written as below"""

print('\n Printing keys without using keys method')
friends=['ahmad','haris']
for name in fav_lan:
    print(name.title())
    
    if name in friends:
        print('Hi',name.title(),'so your fav language is ',fav_lan[name],'!')

#checking if a key is present in a dictionary
""" Can be done with or without using keys() method """

if 'bhutta' not in fav_lan.keys():
    print('Please add bhutta in fav_lan ')

#Looping Through dictionary keys in order
""" Using the sorted() method in for loop """
print('\nUsing sorted method to sort keys in dictionary fav_lan')
for name in sorted(fav_lan.keys()):
    print(name)

#Looping through only values in dictionaries using values() method
print('\nFollowing languages were mentioned by users')
for lan in fav_lan.values():
    print(lan.title())

