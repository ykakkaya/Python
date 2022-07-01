from ast import Num


sayilar = [1,3,5,7,9,12,19,21]

# 1: sayilar listesini while ile ekrana yazdırın.

i=0
while(i<len(sayilar)):
    print(sayilar[i])
    i+=1

print("**************************************")

# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm
#    tek sayıları ekrana yazdırın.

startNum=int(input("başlangıç değerini giriniz"))
finishNum=int(input("bitiş değerini giriniz"))
while(startNum<=finishNum):
    if(startNum%2==1):
        print(startNum)

    startNum+=1


# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.

i=100
while(i>=1):
    print(i)
    i-=1

# 4: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde
#    yazdırın.

num=[]
i=0
while(i<5):
    item=int(input("bir sayı giriniz"))
    num.append(item)
    i+=1
num.sort()
print(num)


# 5: Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
#    ** ürün sayısını kullanıcıya sorun.
#    ** dictionary listesi yapısı (name, price) şeklinde olsun.
#    ** ürün ekleme işlemi bittiğinde ürünleri ekranda for ile listeleyin.

stock=int(input("kaç ürün girişi yapacaksınız: "))

product=[]
i=0
while(i<stock):
    i+=1
    pName=input("ürüm adi: ")
    pPrice=int(input("ürün fiyatı giriniz"))
    product.append ({
        'name':pName,
        'price':pPrice})


for p in product:
    print(f"{p['name']} ürünü fiyatı: {p['price']} ")
    