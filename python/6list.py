#verilen listeleri + ile birleştirebiliriz.
from dataclasses import replace


list1=[1,2,3,4]
list2=[5,6,7,8,'dokuz']
numbers=list1 + list2
print(numbers)
print(len(numbers))
#birleştirme işlemininde liste içinde liste saklamak 

numbers1=[list1,list2]
print(numbers1)
print(numbers1[0])
#alt liste elemanına ulaşmak için
user1=["ahmet",12345]
user2=["veli",98765]
users=[user1,user2]
#birinci kullanıcının parolası
print(users[0][1])
print("***************************************")
s="ALIŞTIRMALAR"
print(s.center(30,"*"))
print("")
#bmw,opel,mercedes,mazda elemanlarına sahip liste olustur.

cars=["bmw","mercedes","opel","mazda"]
print(cars)
print("*****************************************")

#bu liste kaç elemanlıdır

print(len(cars))
print("*****************************************")

#listenin ilk ve son elemanı

print(cars[0])
print(cars[-1])

#mazda değerini toyota ile değiştir

cars[-1]="toyota"
print(cars)
print("*****************************************")

#mercedes listenin bir elemanı mıdır?

result= "mercedes" in cars
print(result)
print("*****************************************")

#listenin -2 indeksindeki değer nedir

print(cars[-2])
print("*****************************************")

#listenin ilk 3 elemanını yazdır

print(cars[0:3])
print("*****************************************")

#listenin son iki elemanı yerine mazda ve renault ekle

cars[-2:]=["mazda","renault"]
print(cars)
print("*****************************************")

#listeye audi ve nissan ekle

cars=cars+["audi","nissan"]
print(cars)
print("*****************************************")
#listenin son elemanını sil

del cars[-1]
print(cars)
print("*****************************************")

#liste elemanlarını tersten yazdır.
print(cars[len(cars)::-1])
# print(::-1) şeklindede yapılabilir
print("*****************************************")

#verilen değerleri liste içinde saklayınız
    # std1= yiğit akkaya ,2016(90,85,95)
    # std2=elif akkaya, 2014 (100,85,95)
    # std3=yakup akkaya ,2008 (85,80,90)

std1=["yiğit", "akkaya" ,2016,[100,85,95]]

print(std1)
std2=["elif" ,"akkaya", 2014,[100,85,95]]

print(std2)
std3=["yakup", "akkaya",2008,[85,80,90]]

bilgi=f"{std2[0]} {std2[1]} öğrencisi {2022-std2[2]} yaşındadır. Not ortalaması {(std2[3][0]+std2[3][1]+std2[3][2])/3} tür."
print(bilgi)

students=[std1,std2,std3]
print(students)