from gettext import find
from importlib.resources import contents
import requests
from bs4 import BeautifulSoup

#url bilgisini giriyoruz

url="https://www.imdb.com/chart/top/?ref_=nv_mv_250"

#request den dönen response content bilgisini alıyoruz
response=requests.get(url)
html= response.content

#content i parse ediyoruz
soup=BeautifulSoup(html,"html.parser")

#dönen sonuçları listeye atıyoruz
list=soup.find("tbody",{"class":"lister-list"}).find_all("tr",limit=50)
count=1

#for döngüsü ile alınan elemanların istrdiğimiz bilgilerine ulaşıyoruz.
for tr in list:
    title= tr.find("td",{"class":"titleColumn"}).find("a").text
    year=tr.find("td",{"class":"titleColumn"}).find("span").text.strip("()")
    rating= tr.find("td",{"class":"ratingColumn imdbRating"}).find("strong").text
    print(f"{count}- {title.ljust(50)} yıl: {year} rating={rating}")
    count+=1