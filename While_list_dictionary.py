            #Using while loop with list and dictionaries

""" Moving items from one list to another """

unconfirmed_users=['happy','sara','john']
confirmed_users=[]

while unconfirmed_users:
    current_user=unconfirmed_users.pop()

    print('Verifying user :',current_user)
    confirmed_users.append(current_user)
    
print('Following user were added in confirmed users',confirmed_users)

#Removing every occurance of an item using while loop

pets=['dog','mice','cat','dog','pigeon','dog','parrot']
print('\nthe original pets list',pets)

while 'dog' in pets:
    pets.remove('dog')

print('\nafter removing every dog item',pets)

#Filling a dictionary with user input

responses={}
flag=True

while flag:
    name=input('\nEnter your name\t')
    place=input('Tell us about your favorite place\t')

    responses[name]=place
    repeat=input('Would you like to enter response for another person\nyes\tno')
    if repeat=='no':
        print('exiting')
        flag=False

for name, place in responses.items():
    print('Name: ',name,'\nfavorite place: ',place)






