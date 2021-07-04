try:
    """We ask python to try running some code here,if code results in perticular kind of
       exception then execute the except block """
    num=5/0

except ZeroDivisionError:
    print("A number cannot be divided by zero")

while True:
    num_1=input("Enter dividend")
    if num_1=='q':
        break

    num_2=input("Enter divider")
    if num_2=='q':
        break

    try:
        answer=int(num_1)/int(num_2)
    except ZeroDivisionError:
        print("The divider cannot be a zero!")
    else:
        print(answer)
        
"""
except:
    print('error occured')
    raise  #using raise statement in except re-raises the error
           #raise can be used outside except block

try:
    print(1/0)
except ZeroDivisionError:
    raise ValueError



name='123'
raise NameError('Invalid Name')
"""
