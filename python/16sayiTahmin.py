'''
   1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile
   buldurmaya çalışın. (hak = 5)
   ** "random modülü" için "python random" şeklinde arama yapın.
   ** 100 üzerinden puanlama yapın. Her soru 20 puan.
   ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı 
      üzerinden hesaplansın.
'''

import math
from random import random

total=100
hak=1
sayi=int(random()*100)
denemeSayısı=int(input("kaç deneme yapmak istersiniz: "))
puan=int(100/denemeSayısı)
while(hak<=denemeSayısı):
    tahmin=int(input("tuttuğum sayıyı tahmin et bir değer gir: "))
    if(tahmin==sayi):
        total=(hak-1)*puan
        print(f"{hak} tahmininizde doğru tahmin ettiniz.deneme sayınız{hak} puanınız{total} ")
        hak=6
    elif(tahmin<sayi):
        print(f"{tahmin} sayısından daha büyük sayı bulmalısınız.deneme sayınız{hak} ")
    elif(tahmin>sayi):
        print(f"{tahmin} sayısınsan daha küçük bir sayı bulmalısınız.deneme sayınız{hak} ")
    
    hak+=1

    if(hak==6):
        print (f"oyun bitti tutulan sayı {sayi} idi")