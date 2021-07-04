import requests

"""
- auth argument tuple is verified against the url parameters
- if no response is recieved 'timeout' will disconnect otherwise
  it will wait forever to get the response
"""
r = requests.get("https://httpbin.org/basic-auth/ahmad/testpass", 
                 auth=('ahmad', 'testpass'), timeout=3)


print(r.text)
print(r)
print(r.status_code)

r1 = requests.get("https://httpbin.org/delay/1", timeout=2)

print(r1)