def char_count(text,char):
    count=0
    for char in text:
        if char==char:
            count+=1
    return count

file_name=input("Enter a filename/File Path: ")
char=str(input('Enter the character to count '))

with open(file_name)as f:
    text=f.read()
    
print(char_count(text,char))

#This for loop checks percentage of every alphabet in the text
for char in "abcdefghijklmnopqrstuvwxyz":
  perc = 100 * char_count(text, char) / len(text)

  #this is string formatting
  print("{0} - {1}%".format(char, round(perc, 2)))

# round command round off the percentage to two decimal places
""" round(perc,2) here perc represent variable to be round off and
    2 defines decimal places"""
