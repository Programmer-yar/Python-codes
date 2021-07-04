# 'shelve' module saves data as dictionary
# data is stored as value specified against a key
import shelve

shelf_file = shelve.open('mydata')
print(shelf_file['colors'])

# colors = ['green', 'blue', 'yellow', 'black', 'red']

# shelf_file['colors'] = colors
shelf_file.close()
