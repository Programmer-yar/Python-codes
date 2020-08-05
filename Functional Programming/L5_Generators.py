                          # Generators
""" iterables like list and tuple
- arbitrary/random indexing is not allowed
- iterated using for loops
- created using functions and for loops
"""

""" Just like electricity generators produce electricity but can't store it
and the produced power can be used instantaneously"""

def countdown(i):
    while i>0:
        yield i      #'yield' used to define a generator and replaces 'return'
        i-=1         # keeps local variable alive which is not the case with 'return'

                     #'yield' used to define a generator and replaces 'return'

""" 'yield' statement yields one item at a time so they have no memory restrictions
like lists"""

for i in countdown(6):
    print(i)

for i in countdown(2):     
    print(list(countdown(3)))
    
for i in countdown(5):
    print(list(countdown(i)))


def get_primes():
    num=2
    while True:
        if is_prime(num):
            yield num
            num+=1

""" generators improve performance because of on demand generation of values
- lower memory usage"""
def numbers(x):
  for i in range(x):
    if i % 2 == 0:
      yield i

print(list(numbers(11)))


def make_word():
  word = ""
  for ch in "spam":
    word +=ch
    yield word

print(list(make_word()))
