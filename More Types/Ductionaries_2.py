                              #Dictionaries part 2
#only immutable objects can be used as key in dictionary

#means key cant be changed but value can be changed
alien_0={'color':'pink','points':5}
print('original alien_0 dictionary',alien_0)
alien_0['color']='red'
print('alien_0 dictionary after changing value of color key')
print(alien_0,'\n')

test={2:4,3:9,4:16}
print(test)
test[6]=36     #adding new "key:value" pair in dictionary
test[2]=test[3]  #changing value of key
test[4]=32
print(test)

info={'ahm':'python','mudassir':'c#'}
print('My fav language is '
      ,info['ahm'].title()
      ,'.')                #we can break print statement in several lines

#Removing key:value pair
del alien_0['color']
print('alien_0 dictionary after deleting "color" key' ,alien_0)

bad_diction={
    [1,2,3]:'one two three',
    }
print(bad_diction['[1,2,3]'])

