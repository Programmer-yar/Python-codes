file=open("C:\\Users\\Ahmad Yar\\Desktop\\test file.txt","w")
#This will delete the file's existing contents if any
#This command will also create a file if it does not exist

size=file.write('helloooo')
print(size)
#this will store the size of written content

file.write('write it again')==len('write it again')
#this command returns the size of written content so it can be comapre with length
#Data other than string should be added by first converting it to string

file.close()

file=open("C:\\Users\\Ahmad Yar\\Desktop\\test file.txt","r")
print(file.read())
file.close()

#closing files in final statement ensures that files will always close
#even if some error occurs
try:
    f=open("C:\\Users\\Ahmad Yar\\Desktop\\test file.txt","r")
    print(f.read())
finally:
    f.close()
