names=["ali","yağmur","hakan","deniz"]
years=[1998,2000,1998,1987]

#cenk ismini listenin sonuna ekleyelim

names.append("cenk")
print(names)
print("**********************")

#"sena" değerini listenin başına ekleyelim

names.insert(0,"sena")
print(names)
print("**********************")

#deniz ismini index ikaçtıe
ind=names.index("deniz")
print(ind)
print("**********************")
#deniz ismini listeden silelim
names.remove("deniz")
print(names)
print("**********************")

#ali listenin bir elemanı mıdır

isIn= "ali" in names
print(isIn)
print("**********************")

#liste elemanlarını tersten yazınız.

names.reverse()
print(names)
print("**********************")
#liste elemanlarını alfabetik sıralayınız
names.sort()
print(names)
print("**********************")

#years listesini sıralayınız
years.sort()
print(years)
print("**********************")


#str ="Dacia,Chevrolet" karakter dizisini listeye çeviriniz
str ="Dacia,Chevrolet"
cars=str.split(',')
print(cars)
print("**********************")
#years dizisinin en büyük ve en küçük elemanı nedir
enBuyuk= min(years)
print(enBuyuk)
enKucuk= max(years)
print(enKucuk)
print("**********************")
#years dizisinde kaç tane 1998 vardır
print(years.count(1998))
print("**********************")
#years dizisinin tüm elemanlarını siliniz
years.clear()
print(years)
print("**********************")
#kullanıcıdan alınan 3 marka bilgisini listede saklayınız

markalar=[]
marka= input("marka giriniz: ")
markalar.append(marka)
marka= input("marka giriniz: ")
markalar.append(marka)
marka= input("marka giriniz: ")
markalar.append(marka)
print(markalar)
