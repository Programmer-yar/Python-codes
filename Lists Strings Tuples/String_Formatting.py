                              #String Formatting
""" A Powerful way to combine non-strings with strings"""
nums=[4,5,6]
msg="Numbers:{0}{1}{2}". format(nums[0],nums[1],nums[2])
print(msg)

msg = "Numbers: {0} {1} {3}". format(4,8,3,6)
print(msg)

print("MyFourLetters: {0[3]}{0[0]}{1[2]}{1[1]}!".format("Abcd","cat"))

print("{0}{1}{0}".format("abra", "cad"))

a="{x},{y}". format(x=5, y=12)
print(a)


str="{c}, {b}, {a}".format(a=5, b=9, c=7)
print(str)
