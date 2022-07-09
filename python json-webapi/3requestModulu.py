from turtle import title
import requests
import json
#önce pypi den requests modülünü yükledik

result=requests.get("https://jsonplaceholder.typicode.com/users/1/todos")
result=json.loads(result.text)

for i in result:
    print(i)
    print(i["id"])
print(result[0]["title"])
