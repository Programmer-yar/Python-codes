import requests

"""To pass url parameters"""
payload = {'page': 2, 'count': 25}

"""
another site used for testing can be 'https://estropical.com/api'
- This is a 'get' request  """
r = requests.get("https://httpbin.org/get", params=payload)

# print(r.text)
# print(r.url)

user_data = {'username': 'ahmad', 'password': 'testpass'}

#This is a 'post' request
r1 = requests.post("https://httpbin.org/post", data=user_data)

#returns a json response
print(r1.text)

#returns a python dictionary from Json format
res_dict = r1.json()
print(res_dict['form'])

