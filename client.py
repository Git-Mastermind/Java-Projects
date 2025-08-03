import requests
url = 'http://192.168.86.24:8080/api/hello'
response = requests.get(url)
print(response.json())
