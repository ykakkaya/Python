sayilar = [1,3,5,7,9,12,19,21]

# 1- Sayilar listesindeki hangi sayılar 3'ün katıdır ?

for sayi in sayilar:
    if(sayi%3==0):
        print(sayi)

print("***********************")
# 2- Sayilar listesinde sayıların toplamı kaçtır ?

toplam=0
for sayi in sayilar:
    toplam+=sayi
print(toplam)

print("***********************")
# 3- Sayilar listesindeki tek sayıların karesini alınız.

for sayi in sayilar:
    if(sayi%2==1):
        print(sayi**2)
print("***********************")

sehirler = ['kocaeli','istanbul','ankara','izmir','rize']

# 4- Şehirlerden hangileri en fazla 5 karakterlidir ?

for city in sehirler:
    if (len(city)<=5):
        print(city)
        
print("***********************")

urunler = [
    {'name':'samsung S6', 'price': '3000' },
    {'name':'samsung S7', 'price': '4000' },
    {'name':'samsung S8', 'price': '5000' },
    {'name':'samsung S9', 'price': '6000' },
    {'name':'samsung S10', 'price': '7000' }
]

# 5- Ürünlerin fiyatları toplamı nedir ?
toplam=0
for p in urunler:
    toplam +=int(p['price']) 
print(toplam)


# 6- Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz ?

for item in urunler:
    if(int(item['price'])<=5000):
        print(f"fiyatı 5000 tl den az ürünler: {item['name']} {item['price']}")