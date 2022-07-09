import requests
import json

kullanici=input("github kullanıcı adını giriniz: ")

target_url="https://api.github.com/users/"+kullanici
result=requests.get(target_url)
print(result)
result=json.loads(result.text)

print(f"Kullanıcı adı: {result['login']}")
print(f"url adresi: {result['html_url']}")
print(f"kullanıcı tam adı: {result['name']}")
print(f"kullanıcı şirket bilgisi: {result['company']}")
print(f"kullanıcı ilgi alanları: {result['bio']}")