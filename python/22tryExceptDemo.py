

from math import factorial


liste = ["1","2","5a","10b","abc","10","50"]

# 1: Liste elemanları içindeki sayısal değerleri bulunuz.
numbers=[]
try:
    for item in liste:
        if(item.isnumeric()):
            numbers.append(item)
    print(numbers)
except Exception as ex:
    print(ex)


# 2: Kullanıcı 'q' değerini girmedikçe aldığınız her inputun sayı 
# olduğundan emin olunuz aksi halde hata mesajı yazın.
items=[]
start=True
try:
    while (start<7):
        
        item=input("bir değer giriniz.çıkmak için 'q' ya basınız: ")
        if(item=='q'):
            break
        else:
            if(item.isnumeric()):
                items.append(item)
            else:
                print(f"gelen değer numeric olmalı girilen değer {item}")
except Exception as ex:
    print(ex)
else:
    print(items)


# 3: Girilen parola içinde türkçe karakter hatası veriniz.

def checkPassword(password):
    import re
    if re.search("[ğÜİçÖ]",password):
        raise Exception("türkçe karakter kullanmayınız")

s=True
while(s):
    passw=input("parolanızı giriniz")
    try:
        checkPassword(passw)
    except Exception as e:
        print(e)
    else:
        print("giriş başarılı")
        s=False
# 4: Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için
# hata mesajları verin.

def faktoriyl(number):
    import math
    result=factorial(number)
    
    print(f"{number} değerinin faktoriyeli {result} dır")

fakt=True
while(fakt):
    try:    
        num=input("bir sayı biriniz çıkmak için 'q' ya basınız: ")
        if(num.isnumeric()):
           faktoriyl( int(num))
        elif(num=='q'):
            fakt=False
        else:
            raise Exception("girilen değer sayı olmalıdır.")
    except Exception as e:
        print(e)
        

