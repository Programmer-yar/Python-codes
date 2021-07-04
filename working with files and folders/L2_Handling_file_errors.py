                        #Handling file not found errors
file_name='alice.txt'
try:
    with open(file_name) as file:
        print(file.read())

except FileNotFoundError:
    msg="the file"+" "+file_name+" "+"does not exist"
    print(msg)
    
    

