from cgitb import text
from gettext import find
from bs4 import BeautifulSoup
import requests

#n11 sitesi lenova bilgisayarların isim ve fiyat bilgileri

url="https://www.n11.com/bilgisayar/dizustu-bilgisayar?m=Lenovo"
response=requests.get(url=url)
html=response.content
soup=BeautifulSoup(html,"html.parser")
list=soup.find_all("li",{"class":"column"},limit=20)
count=1
for item in list:
    title=item.find("h3",{"class":"productName"}).text
    price=item.find("input",{"class":"advantageDeliveryDiscountedPrice"}).get("value")
    print(f"{count}-{title} = {price}")
    count +=1
   



