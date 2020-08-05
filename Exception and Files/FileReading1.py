len(open("C:\\Users\\Ahmad Yar\\Desktop\\test file.txt").readlines())

file=open("C:\\Users\\Ahmad Yar\\Desktop\\test file.txt","r")
for line in file:
    print(line)
file.close()

file=open("C:\\Users\\Ahmad Yar\\Desktop\\test file.txt","r")
print(file.readlines())
print(file.read(4))

name=file.read()
print(len(name))  #will show length of rest of document
file.close()


