                     #Dictionaries part 4
""" recommendation: Avoid deep nesting of list, dictionaries
as this will make the task at hand complex while it can be done in a simpler way"""

alien_0={'color':'red','points':'5'}
alien_1={'color':'blue','points':'10'}
alien_2={'color':'green','points':'15'}

#A list of dictionaries or dictionaries inside of a list
aliens=[alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

alien_fleet=[]
for c in range(30):
    new_alien={'color':'green','points':'5'}
    alien_fleet.append(new_alien)

print('\ntotal number of created aliens are',len(alien_fleet),
      '\nfirst 5 aliens are',alien_fleet[:5])
    
for alien in alien_fleet[:3]:
    alien['color']='blue'
    alien['points']='10'
    alien['speed']='medium'

print('\nAfter cahnging the first 3 aliens\n')
for show in alien_fleet[:5]:
    print(show)

#A dictionary of lists or lists inside of a dictionary
pizza={'crust':'thick','topings':['extra cheese','olives','mushrooms']}
print('\nyou ordered a pizza with',pizza['crust']+'-crust and with topings as below')
for toping in pizza['topings']:
    print(toping)

fav_lan={'happy':['python'],'ahmad':['python','c++','Java Script'],'haris':['python','swift']}
for name, lang in fav_lan.items():
    if len(lang)==1:
        print('\nFavorite language of',name.title(),'is')
    elif len(lang)>1:
        print('\nFavorite languages of',name.title(),'are')
    for c in lang:
        print(c.title())

#A dictionary in a dictionary
user_data={'ahmyar':
           {'first':'ahmad',
            'last':'yar',
            'location':'multan'},
           
           'aeinstein':
           {'first':'albert',
            'last':'einstein',
            'location':'princeton'}
           }

for name,info in user_data.items():

#info will contain another dictionary
    
    print('\nUser Name:',name)
    print('first name:',info['first'],
          'last name:',info['last'],
          'location:',info['location'])


