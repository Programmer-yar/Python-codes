                                #List Functions
nums=[55,44,33,22,11]

if all([i>5 for i in nums]):
    print('all larger than 5')

if any([i%2==0 for i in nums]):
    print('atleast one even in nums list')

#This command will give (index,element) pair for the entire list e.g(0,-1)
for v in enumerate(nums):
    print(v)


nums = [-1, 2, -3, 4, -5]
if all([abs(i) < 3 for i in nums]):
  print(1)
else:
  print(2)
