import requests
import json

bozulan=input("hangi döviz cinsini bozduracaksınız? ")
alınan=input("ne alacaksınız? ")
miktar=int(input("ne kadar bozduracaksınız? "))

doviz_url="https://api.exchangeratesapi.io/latest?base="+bozulan
result=requests.get(doviz_url)
result=json.loads(result.text)
doviz=(result["rates"][alınan])*miktar
print(f"{miktar} {bozulan} {doviz} {alınan} etmektedir.")
