print(1)
assert 2+2==4
print(2)
assert 1+1==3  #assertion error will terminate the program
print(3)
assert True
print(4)

#run this part seperately
temp=-10
assert(temp>=0), "Colder than absolute zero"

"""first argument of above assertion is (temp>=0)
while second argument is "colder than absolute zero"
"""

#run this part seperately
def my_func(x):
    assert x>0,"Error!"
    print(x)
