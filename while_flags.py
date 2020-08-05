                   #while loops using flags
prompt='Enter exit if you want to end this loop\n'
prompt+='Tell us something we will tell it back:\n'
msg=''
while msg!='exit':
    msg=input(prompt)

    if msg!='exit':
        print(msg)


print('this is the end of first loop without a flag\n')

# When many possible events need to be tested a flag is used
""" instead of testing all conditions inside of a while loop and
complicating the program
- we use flag to test all conditions and hold only one condition i.e
True or False"""

active=True
while active:
    msg=input(prompt)

    if msg=='exit':
        active=False
    else:
        print(msg)
