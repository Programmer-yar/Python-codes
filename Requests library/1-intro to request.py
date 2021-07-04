import requests

r = requests.get('https://xkcd.com/353/')

#a response object will be returned
# 'r' is a 'Response' object
#To get all attributes of the object use "dir(object)"
print(dir(r))

#if there is no problem will return true
print(r.ok)

#returns the status code of the server
print(r.status_code)

"""to get headers """
print('Headers', r.headers)

"""To get complete information about a class """
print(help(r))

""" returns source code of the webpage """
print(r.text)

r1 = requests.get('https://imgs.xkcd.com/comics/python.png')


"""to download an image in bytes """
print(r1.content)

"""
to download and save the image
open/create a 'png' file as 'write byte' wb mode
"""

# with open('comic.png', 'wb') as f:
#     f.write(r1.content)

