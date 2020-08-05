                    #While loop with break statement
i=0
while True:
    i=i+1
    if i==2:
        print('skipping 2')
        continue
    if i==5:
        print('breaking')
        break
    print(i)

print('finished')

while True:
    city=input('please enter the name of the city you live in: ')
    if city=='quit':
        break
    else:
        print(city)

             #While loop with continue statement

current_number=0
while current_number < 10:
    current_number+=1
    if current_number % 2==0:
        continue             #ignores rest of the loop code and returns to begining

    print(current_number)
