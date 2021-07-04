                        #Dictionaries part 1
"""- dictionaries are data structures and map arbitrary values
- each element in dictionary is a "key:value" pair
- are indexed in the same way as lists but square brackets contain keys
- can store any types of data""" 
ages={"Ramay":24,"me":25,"hassaan":8,"ghoofi":4,'1':23,"our car":"white"}
print(ages["me"])
print(ages['1'])
print(ages['our car'])


#the value of a key can be stored in another variable by calling that key
my_car_color=ages['our car']
print('My car color is '+my_car_color)

#adding new key:value pair in existing dictionary
alien_0={'color':'green','points':5}
print('the original alien_0 dictionary \t',alien_0)
alien_0['x_pos']=0
alien_0['y_pos']=25
print('the alien dictionary after adding two more pairs',alien_0)

#in key:value pair value may contain list, another dictionary or tuple
primary={'red':[255,0,0],
         'green':[0,255,0],
         'blue':[0,0,255],
         }
print(primary['red'])

#defining empty dictionary and adding values afterwards
""" empty dictionaries are mostly used to store user generated data or
- automated generated data by some code"""

alien_1={}
print('the empty dictionary alien_1 ',alien_1)
alien_1['color']='blue'
alien_1['points']=10
print('the dictionary alien_1 after adding 2 key:value ',alien_1)

