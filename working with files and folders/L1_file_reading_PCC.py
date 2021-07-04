from collections import Counter

file_path="C:\\Users\\Ahmad Yar\\Desktop\\test file.txt"
with open(file_path) as file:
    data=file.read()
    print(data.rstrip(), "\n")

# strip() method
"""
- 'strip()' method removes spaces from both sides of a string
- 'lstrip()' and 'rstrip()' remove spaces from left and right sides respectively
"""

                      #Reading Line by Line
with open(file_path) as file:
    for line in file:
        print(line)

        """ the output will have two new lines
            - invisible new line character in the text file
            - print statement also inserts a new line
            - use rstrip() to eliminate those lines """
        
with open(file_path) as file:
    print("\nWith 'rstrip()' eliminating blank lines\n") 
    for line in file:
        print(line.rstrip())

              #Making a list of lines from file
py_test_file="C:\\Users\\Ahmad Yar\\Desktop\\py test file.txt"
with open(py_test_file) as file_1:
    lines=file_1.readlines()

print("\nMaking a list of lines inside with statement and using it later\n")
for line in lines:
    print(line)

              #Working with a file's content
with open(file_path) as file:
    lines=file.readlines()

pi_string=""
for line in lines:
    pi_string+=line.strip()

print(pi_string)
print(len(pi_string))

#working with pi uptill 1M digits
pi_path="C:\\Users\\Ahmad Yar\\Desktop\\pi.txt"
with open(pi_path) as pi:
    lines=pi.readlines()

pi_string=""
for line in lines:
    pi_string+=line.strip()

my_b_date='090905'

if my_b_date in pi_string:
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*",
          "\nHurrah, your birthday was found in first million digits of pi\n",
          "-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

else:
    print("Your birthday is not present in first million",
          "digits of pi")



print('\n', len(pi_string))

cnt_pi_string=Counter(pi_string)

print(cnt_pi_string['1']) #returns the count of 1 in first million of pi
print(cnt_pi_string.most_common())

# replace method for string
my_pet="I love dogs"
ch_my_pet=my_pet.replace('dogs', 'cats')
print(ch_my_pet)



