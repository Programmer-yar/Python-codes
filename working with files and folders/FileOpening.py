with open("C:\\Users\\Ahmad Yar\\Desktop\\test file.txt") as file:
    print(file.read())

#read mode
file=open("C:\\Users\\Ahmad Yar\\Desktop\\test file.txt","r")
content=file.read()
print(content)
file.close()

#write mode
open("C:\\Users\\Ahmad Yar\\Desktop\\test file.txt","w")

#do stuff
file.close()
#closes the file

#read mode
open("C:\\Users\\Ahmad Yar\\Desktop\\test file.txt","r")

#binary write mode
open("C:\\Users\\Ahmad Yar\\Desktop\\test file.txt","wb")
#binary read mode

