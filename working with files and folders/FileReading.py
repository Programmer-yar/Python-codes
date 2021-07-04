#read mode
file=open("C:\\Users\\Ahmad Yar\\Desktop\\test file.txt","r")
print(file.read(5))   #will print first five letters,
print(file.read(10))   #will print next five letters including spaces

"""
These commands will print the content of required file, while argument in
file.read(5) specifies the amount in bytes. 1 byte= 1 character/8 bits
"""

print(file.read())  #will print rest of the document
print(file.read(-1)) #passing negative arguments also prints the whole or
                     #rest of the file
print('will try to reread it now')
print(file.read())
print("you will notice empty space if its already been read")

